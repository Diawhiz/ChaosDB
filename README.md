# ChaosDB

**Version**: 0.1 (Pre-alpha)  
**License**: MIT License  
**Last Updated**: October 25, 2025  

## Description
ChaosDB is an innovative, open-source, secure database system designed for unpredictable data storage and robust access control. It leverages advanced cryptography (AES-256-GCM), secure authentication (Argon2 and JWT), and a user-friendly three-letter command-line interface (CLI) with commands like `put`, `get`, `del`, `rem`, `log`, and `reg`. Ideal for developers and organizations needing a decentralized, scalable database, ChaosDB integrates with Django and blockchain platforms (e.g., Ethereum). This project welcomes community contributions to enhance its features, security, and usability.

## Features
- **Chaotic Data Storage**: Uses sharded hash tables and B+ trees for unpredictable data placement.
- **Secure Authentication**: Implements Argon2 password hashing and JWT-based session management.
- **Simple CLI**: Three-letter commands for ease of use (`put`, `get`, `del`, `rem`, `log`, `reg`).
- **Cryptographic Strength**: AES-256-GCM with HKDF for data encryption and key derivation.
- **Extensibility**: Supports integration with Django and blockchain technologies.
- **Backup and Logging**: Includes automated backups and event logging.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chaosdb.git
   cd chaosdb
