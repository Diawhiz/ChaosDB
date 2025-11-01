

import os
import json
import argon2
import jwt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import time
import shutil

class ChaosDB:
    def __init__(self, backup_dir="backups"):
        # Initialize core structures
        self.data_store = {}  # Sharded hash table
        self.users = {}  # username -> (hashed_password, salt, role)
        self.tokens = {}  # token -> (username, expiry)
        self.master_key = os.urandom(32)
        self.private_key = os.urandom(32)
        self.log_file = "chaosdb.log"
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)
        self.load_backup()  # Load last backup on startup

    def _derive_key(self, password, salt):
        """Derive encryption and authentication keys."""
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            info=b'chaosdb-auth'
        )
        return hkdf.derive(password.encode())

    def reg(self, username, password):
        """Register a new user with role assignment."""
        if username in self.users:
            self.log("Registration failed: User exists")
            return False
        salt = os.urandom(16)
        hasher = argon2.PasswordHasher()
        hashed_pw = hasher.hash(password, salt=salt)
        self.users[username] = (hashed_pw, salt, 'user')  # Default role
        self.log(f"User {username} registered")
        self.backup()
        return True

    def log(self, username, password):
        """Login and issue a JWT."""
        if username not in self.users:
            self.log("Login failed: User not found")
            return None
        hashed_pw, salt, _ = self.users[username]
        hasher = argon2.PasswordHasher()
        try:
            hasher.verify(hashed_pw, password)
        except argon2.exceptions.VerifyMismatchError:
            self.log("Login failed: Wrong password")
            return None
        payload = {"username": username, "exp": time.time() + 86400, "role": self.users[username][2]}
        token = jwt.encode(payload, self.private_key, algorithm="HS256")
        self.tokens[token] = (username, time.time() + 86400)
        self.log(f"User {username} logged in")
        return token

    def validate_token(self, token):
        """Validate JWT and check role."""
        try:
            payload = jwt.decode(token, self.private_key, algorithms=["HS256"])
            if token not in self.tokens or time.time() > self.tokens[token][1]:
                self.log("Token validation failed: Expired")
                return None
            self.tokens[token] = (payload["username"], time.time() + 86400)
            return payload["username"], payload["role"]
        except jwt.InvalidTokenError:
            self.log("Token validation failed: Invalid")
            return None, None

    def put(self, key, data, token):
        """Insert data with role-based access."""
        username, role = self.validate_token(token)
        if not username or role not in ['user', 'admin']:
            self.log("Put failed: Unauthorized")
            return
        data_key = Fernet.generate_key()
        encrypted_data = Fernet(data_key).encrypt(data.encode())
        self.data_store[key] = (encrypted_data, data_key)
        self.log(f"Data stored by {username} under key: {key}")
        self.backup()

    def get(self, key, token):
        """Retrieve data with role check."""
        username, role = self.validate_token(token)
        if not username or role not in ['user', 'admin']:
            self.log("Get failed: Unauthorized")
            return
        if key not in self.data_store:
            self.log("Get failed: Key not found")
            return
        encrypted_data, data_key = self.data_store[key]
        decrypted_data = Fernet(data_key).decrypt(encrypted_data).decode()
        self.log(f"Data retrieved by {username} for key: {key}")
        return decrypted_data

    def del_(self, key, token):
        """Delete data with admin-only access."""
        username, role = self.validate_token(token)
        if not username or role != 'admin':
            self.log("Delete failed: Admin access required")
            return
        if key in self.data_store:
            del self.data_store[key]
            self.log(f"Data deleted by {username} for key: {key}")
            self.backup()

    def rem(self, key, token):
        """Alias for delete."""
        self.del_(key, token)

    def backup(self):
        """Create a backup of the data store."""
        backup_file = os.path.join(self.backup_dir, f"backup_{int(time.time())}.json")
        with open(backup_file, 'w') as f:
            json.dump({k.decode(): v[0].decode() for k, v in self.data_store.items()}, f)
        self.log(f"Backup created: {backup_file}")

    def load_backup(self):
        """Load the latest backup."""
        backup_files = [f for f in os.listdir(self.backup_dir) if f.startswith("backup_")]
        if backup_files:
            latest = max(backup_files)
            with open(os.path.join(self.backup_dir, latest), 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    self.data_store[k.encode()] = (v.encode(), Fernet.generate_key())
            self.log(f"Loaded backup: {latest}")

    def log(self, message):
        """Log events to file."""
        with open(self.log_file, 'a') as f:
            f.write(f"{time.ctime()}: {message}\n")

    def promote_user(self, username, token):
        """Promote user to admin (admin-only)."""
        admin_username, role = self.validate_token(token)
        if not admin_username or role != 'admin':
            self.log("Promotion failed: Admin access required")
            return
        if username in self.users:
            _, _, _ = self.users[username]
            self.users[username] = (self.users[username][0], self.users[username][1], 'admin')
            self.log(f"User {username} promoted to admin by {admin_username}")
            self.backup()

