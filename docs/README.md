# ChaosDB

[![Version](https://img.shields.io/badge/version-0.1--pre--alpha-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)]()

**Version:** 0.1 (Pre-alpha)  
**License:** MIT License  
**Last Updated:** November 1, 2025

---

## Description

ChaosDB is an innovative, open-source, secure database system designed for unpredictable data storage and robust access control. It leverages advanced cryptography (AES-256-GCM), secure authentication, and modular extensibility for modern applications.

---

## Features

- **Chaotic Data Storage:** Uses sharded hash tables and B+ trees for unpredictable data placement.
- **Secure Authentication:** Implements Argon2 password hashing and JWT-based session management.
- **Simple CLI:** Three-letter commands for ease of use (`put`, `get`, `del`, `rem`, `log`, `reg`).
- **Cryptographic Strength:** AES-256-GCM with HKDF for encryption and key derivation.
- **Extensibility:** Integration support for Django and blockchain technologies.
- **Backup and Logging:** Automated backups and event logging.

---

## Installation

```bash
git clone https://github.com/diawhiz/chaosdb.git
cd chaosdb
pip install -r requirements.txt
```

---

## Usage

### CLI Commands

- `reg <username> <password>` &mdash; Register a new user.
- `log <username> <password>` &mdash; Log in and get a token.
- `put <key> <data>` &mdash; Insert data (requires token).
- `get <key>` &mdash; Retrieve data (requires token).
- `del <key>` &mdash; Delete data (admin token required).
- `rem <key>` &mdash; Alias for `del` (admin token required).
- `exit` &mdash; Exit the CLI.

#### Example Session

```shell
$ python main.py
Enter command (reg, log, put, get, del, rem, exit): reg user1 securepass123
User registered
Enter command (reg, log, put, get, del, rem, exit): log user1 securepass123
Logged in, token: <token>
Enter command (reg, log, put, get, del, rem, exit): put key1 Sensitive data
Data stored under key: key1
Enter command (reg, log, put, get, del, rem, exit): get key1
Data: Sensitive data
```

---

## Project Structure

```
chaosdb/
├── chaosdb/              # Main package
│   ├── __init__.py
│   ├── core.py           # ChaosDB class implementation
│   ├── blockchain.py     # Blockchain integration
│   ├── cli.py            # CLI implementation
│   └── tests/            # Unit tests
│       ├── test_core.py
│       └── test_blockchain.py
├── docs/                 # Documentation
│   ├── README.md
│   └── CONTRIBUTING.md
├── backups/              # Backup directory
├── chaosdb.log           # Log file
├── requirements.txt      # Dependencies
├── setup.py              # Installation script
├── LICENSE               # MIT License
├── main.py               # Entry point for CLI
```

---

## Requirements

- Python 3.8+
- Dependencies (in `requirements.txt`):
  - argon2-cffi
  - jwt
  - cryptography

---

## Security

- All data encrypted at rest with AES-256-GCM.
- Secure key derivation using HKDF.
- Passwords hashed with Argon2.
- JWT tokens for session management.

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](chaosdb/docs/CONTRIBUTING.md) for guidelines.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

- **Maintainer:** Ariyo Israel Gbemisola
- **Email:** igbemisola53@gmail.com
- **GitHub:** [github.com/diawhiz](https://github.com/diawhiz)

---

## Roadmap

- Add multi-node sharding support
- Enhance blockchain integration with smart contract testing
- Implement a web-based interface
- Improve documentation and tutorials

---

Thank you for your interest in ChaosDB!  
Let's build a secure future together.
