---

# ChaosDB  
**Version**: 0.1 (Pre-alpha)   
**License**: MIT License   
**Last Updated**: October 31, 2025    

## Description 
ChaosDB is an innovative, open-source, secure database system designed for unpredictable data storage and robust access control. It leverages advanced cryptography (AES-256-GCM), secure authentication (Argon2 and JWT), and a user-friendly three-letter command-line interface (CLI) with commands like `put`, `get`, `del`, `rem`, `log`, and `reg`. Ideal for developers and organizations needing a decentralized, scalable database, ChaosDB integrates with Django and blockchain platforms (e.g., Ethereum). 
This project welcomes community contributions to enhance its features, security, and usability.  

## Features 
- **Chaotic Data Storage**: Uses sharded hash tables and B+ trees for unpredictable data placement. 
- **Secure Authentication**: Implements Argon2 password hashing and JWT-based session management. 
- **Simple CLI**: Three-letter commands for ease of use (`put`, `get`, `del`, `rem`, `log`, `reg`). 
- **Cryptographic Strength**: AES-256-GCM with HKDF for data encryption and key derivation. 
- **Extensibility**: Supports integration with Django and blockchain technologies. 
- **Backup and Logging**: Includes automated backups and event logging.  

## Installation 
1. Clone the repository:    bash
   git clone https://github.com/diawhiz/chaosdb.git
   cd chaosdb
2. Install dependencies:   bash
   pip install -r requirements.txt
3. Run the CLI:   bash
   python main.py
    
## Usage 
### CLI Commands 
- `reg <username> <password>`: Register a new user. 
- `log <username> <password>`: Log in and get a token. 
- `put <key> <data>`: Insert data (requires token). 
- `get <key>`: Retrieve data (requires token). 
- `del <key>`: Delete data (requires admin token). 
- `rem <key>`: Alias for `del` (requires admin token). 
- `exit`: Exit the CLI.  

### Examplebash
$ python main.py
Enter command (reg, log, put, get, del, rem, exit): reg user1 securepass123
User registered
Enter command (reg, log, put, get, del, rem, exit): log user1 securepass123
Logged in, token: <token>
Enter command (reg, log, put, get, del, rem, exit): put key1 Sensitive data
Data stored under key: key1
Enter command (reg, log, put, get, del, rem, exit): get key1
Data: Sensitive data

 ## Project Structure
chaosdb/
│
├── chaosdb/                # Main package
│   ├── init.py
│   ├── core.py            # ChaosDB class implementation
│   ├── blockchain.py      # Blockchain integration
│   ├── cli.py             # CLI implementation
│
├── tests/                  # Unit tests
│   ├── test_core.py
│   ├── test_blockchain.py
│
├── docs/                   # Documentation
│   ├── README.md          # This file
│   ├── CONTRIBUTING.md    # Contribution guidelines
│
├── backups/                # Backup directory
│
├── chaosdb.log             # Log file
│
├── requirements.txt        # Dependencies
├── setup.py                # Installation script
├── LICENSE                 # MIT License
├── main.py                 # Entry point for CLI

 ## Requirements 
 - Python 3.8+ 
 - Dependencies listed in `requirements.txt`:   
    - `argon2-cffi`   
    - `jwt`   
    - `cryptography` 
 
 ## Contributing 
 We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on how to contribute.  
 
 ## License 
 This project is licensed under the MIT License 
 - see the [LICENSE](LICENSE) file for details.  
 
 ## Contact 
 - **Maintainer**: [Ariyo Israel Gbemisola]  
 - **Email**: igbemisola53@gmail.com   
 - **GitHub**: [github.com/diawhiz](https://github.com/diawhiz)  
 
 ## Roadmap 
 - Add multi-node sharding support. 
 - Enhance blockchain integration with smart contract testing. 
 - Implement a web-based interface. 
 - Improve documentation and tutorials.  

Thank you for your interest in ChaosDB! Let's build a secure future together.

---