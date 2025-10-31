import os 
import Json 
import argon2
import jwt
from cryptography.fernet import fernet
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import time

class ChaosDB:
    def __init__(self, backup_dir="backups"):
        #initialize core struture
        self.data_store{} #sharded hash table
        self.user = {} #username ->(hash_password, salt, role)
        self.tokens = {}  # token -> (username, expiry)
        self.master_key = os.urandom(32)
        self.private_key = os.urandom(32)
        self.log_file = "chaosdb.log"
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)
        self.load_backup()  # Load last backup on startup