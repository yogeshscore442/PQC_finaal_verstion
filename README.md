# 🛡️ PQC Secure Communication - Post-Quantum Cryptography Platform

Repository: `PQC_finaal_verstion`

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white)
![NIST PQC](https://img.shields.io/badge/NIST%20PQC-FIPS%20203%2F204%2F205-00C853?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Quantum--Resistant-FF3D00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <b>A complete post-quantum cryptography platform for secure communication using NIST-approved quantum-resistant algorithms.</b>
</p>

**Secure Chat • Encrypted Email • Protected File Vault • Quantum Signatures • PQC Key Exchange**

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Why Post-Quantum Cryptography](#why-post-quantum-cryptography)
- [Architecture & Algorithms](#architecture--algorithms)
- [Installation](#installation)
- [Usage](#usage)
- [Security Features](#security-features)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Technical Stack](#technical-stack)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**PQC Secure Communication** is a modern web-based platform that implements **Post-Quantum Cryptography (PQC)** standards approved by NIST (National Institute of Standards and Technology). 

### What This Project Does:
- ✅ Provides quantum-resistant encryption for real-time communications
- ✅ Uses NIST-standardized PQC algorithms (FIPS 203, 204, 205)
- ✅ Protects against both classical and future quantum computing threats
- ✅ Offers practical tools for secure messaging, email, and file storage
- ✅ Includes live attack simulation and security visualization

### The Problem We Solve:
Today's encryption (RSA, ECC) will be broken by quantum computers. Hackers are already collecting encrypted data to decrypt later ("harvest now, decrypt later" attacks). This project provides **future-proof encryption** that remains secure even against quantum computers.

---

## Features

### 💬 **Real-Time Quantum Chat**
- End-to-end encrypted messaging with post-quantum key exchange
- Support for individual and group conversations
- Online/offline user status tracking
- Message delivery confirmation

### 📧 **Quantum-Encrypted Email**
- PQC-secured email with digital signatures
- File attachment encryption
- Sender authentication via ML-DSA quantum signatures
- Quantum-safe key exchange for async communication

### 📁 **Secure File Vault**
- AES-256-GCM file encryption
- SHA3-384 integrity verification
- Encrypted storage with secure download
- Support for large file uploads

### 🔬 **Live Cyber Attack Simulation**
- Real-time tampering attack demo
- Replay attack testing
- Man-in-the-Middle (MITM) defense showcase
- Authentication failure visualization

### 🔐 **Quantum Signatures & Handshakes**
- ML-DSA-65 (Dilithium) digital signatures
- ML-KEM-768 hybrid key encapsulation
- X25519 elliptic curve key exchange
- Perfect Forward Secrecy (PFS) support

### 📊 **Performance Monitoring**
- Real-time cryptographic operation benchmarks
- KeyGen, Encrypt, Decrypt, Sign performance metrics
- Classical vs Quantum algorithm comparison
- Latency and throughput analysis

---

## Why Post-Quantum Cryptography?

| Aspect | Classical (RSA/ECC) | Post-Quantum (Our System) |
|--------|-------------------|------------------------|
| **Quantum Threat** | ❌ Broken by quantum computers | ✅ Mathematically resistant |
| **Standards** | Becoming obsolete (NIST, 2030) | ✅ NIST FIPS 203/204/205 approved |
| **Security Level** | Single-layer protection | ✅ Hybrid dual-layer (X25519 + ML-KEM) |
| **Future Proof** | No | ✅ Yes (safe for 50+ years) |
| **Harvest Now, Decrypt Later Safe** | No | ✅ Yes |

### Timeline of Threat:
- **2024-2030:** Quantum computers still developing
- **2030+:** Large-scale quantum computers emerge
- **Future:** All current RSA/ECC encrypted data is vulnerable
- **Our Solution:** Protected today, tomorrow, and beyond

---

## Architecture & Algorithms

### 🔑 Key Exchange (ML-KEM-768 + X25519 Hybrid)
```
Purpose: Establish a shared secret key between two users
Hybrid Approach:
  ├─ X25519: Classical elliptic curve (fast, efficient)
  └─ ML-KEM-768: Post-quantum lattice (quantum-resistant)
Result: Two independent keys are combined (XOR) for maximum security
```

### 🔐 Encryption (AES-256-GCM + ChaCha20-Poly1305)
```
Purpose: Encrypt the actual message data
AES-256-GCM:
  ├─ 256-bit key strength
  ├─ Galois/Counter Mode for authentication
  └─ 16-byte authentication tag
ChaCha20-Poly1305:
  ├─ Stream cipher alternative
  └─ Built-in Poly1305 MAC
```

### ✍️ Digital Signatures (ML-DSA-65 + SLH-DSA)
```
Purpose: Prove sender identity and prevent impersonation
ML-DSA-65 (Dilithium):
  ├─ Module-lattice based
  ├─ ~2.4KB signature size
  └─ NIST FIPS 204 approved
SLH-DSA (SPHINCS+):
  ├─ Stateless hash-based backup
  └─ Emergency authentication
```

### 🔄 Key Derivation (HKDF-SHA-384)
```
Purpose: Derive cryptographic keys from shared secrets
- Extract: Condense random input
- Expand: Generate required key material
- Salt: Prevents rainbow table attacks
- Info: Context-dependent key separation
```

### Algorithm Stack Summary:
```
┌─────────────────────────────────────────────────────────────────┐
│                     CRYPTOGRAPHIC SUITE                         │
├──────────────────┬──────────────────┬──────────────────────────┤
│ Key Exchange     │ Signatures       │ Encryption               │
├──────────────────┼──────────────────┼──────────────────────────┤
│ • ML-KEM-768     │ • ML-DSA-65      │ • AES-256-GCM            │
│ • X25519         │ • SLH-DSA        │ • ChaCha20-Poly1305      │
│ • HKDF-SHA-384   │ • SHA3-384       │ • HMAC-SHA-384           │
│ • SHA3-384       │                  │ • NONCE generation       │
└──────────────────┴──────────────────┴──────────────────────────┘
```

---

## Installation

### System Requirements:
- **OS:** Windows 10/11, Linux, or macOS
- **Python:** 3.10, 3.11, 3.12, or 3.13
- **RAM:** Minimum 2GB (4GB+ recommended)
- **Disk Space:** 500MB for dependencies

### Step 1: Clone the Repository
```bash
git clone https://github.com/yogeshscore442/PQC-Secure-Communication-.git
cd PQC-Secure-Communication-
```

### Step 2: Install Dependencies

#### Windows (Automatic):
Double-click `INSTALL_DEPENDENCIES.bat`

#### Windows (Manual):
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python -c "from app import create_app; print('✅ Installation successful!')"
```

---

## Usage

### Start the Application

#### Windows (Automatic):
Double-click `START_SERVER.bat`

#### Windows/Linux/macOS (Manual):
```bash
python run.py
```

The server will start on `http://localhost:5000`

### Access from Different Devices:
When the server starts, it displays:
```
🚀 Local Access:    http://localhost:5000
📱 Wi-Fi/LAN IP:    http://192.168.1.X:5000
```

Open the LAN IP on another device (phone, tablet, laptop) to test secure communication between devices.

### Core Modules:

1. **Chat Module** (`app/chat/`)
   - Real-time WebSocket communication
   - Quantum-safe key exchange
   - Message encryption and verification

2. **Auth Module** (`app/auth/`)
   - User registration and login
   - Secure session management
   - Password hashing (Argon2)

3. **Crypto Module** (`app/crypto/`)
   - ML-KEM key encapsulation
   - ML-DSA signature generation/verification
   - AES-256-GCM encryption
   - Hybrid key derivation

4. **Email Module** (`app/mail/`)
   - Quantum-encrypted email
   - Async encryption/decryption
   - Secure attachments

5. **File Module** (`app/files/`)
   - Encrypted file upload/download
   - SHA3-384 integrity verification
   - Streaming cipher support

6. **API Module** (`app/api/`)
   - RESTful endpoints
   - JSON request/response handling
   - Error handling and logging

---

## Security Features

### 🛡️ Defense Mechanisms:

1. **Quantum-Resistant Encryption**
   - Lattice-based mathematics (ML-KEM-768)
   - Resistant to Shor's algorithm
   - NIST-approved standards

2. **Authentication Tag (AES-GCM)**
   - 16-byte tag detects tampering
   - Fails on any bit modification
   - Automatic packet rejection

3. **Replay Attack Prevention**
   - Monotonic sequence numbers
   - Timestamp verification
   - Session nonce binding

4. **Man-in-the-Middle (MITM) Protection**
   - ML-DSA digital signatures
   - Sender authentication
   - Unforgeable signatures

5. **Perfect Forward Secrecy (PFS)**
   - Unique key per session
   - Past sessions unaffected by key leakage
   - Ephemeral key exchange

6. **Key Derivation Security**
   - HKDF-SHA-384 with salt
   - Context-dependent expansion
   - 256-bit entropy guarantee

---

## Testing

### Run Automated Tests:
```bash
# Run all tests
pytest tests/

# Run specific test module
pytest tests/test_crypto.py -v

# Run with coverage
pytest --cov=app tests/
```

### Available Tests:

| Test File | Purpose |
|-----------|---------|
| `test_crypto.py` | Cryptographic function validation |
| `test_chat_advanced_features.py` | Chat encryption and signatures |
| `test_integration.py` | End-to-end communication flows |
| `test_real_crypto_attacks.py` | Attack simulation and defense |
| `test_group_and_delete.py` | Group chat and cleanup |

### Manual Security Testing:

1. **Handshake Test:**
   - Open browser DevTools (F12)
   - Execute Handshake between two users
   - Verify shared secret key in console logs

2. **Tamper Detection:**
   - Check "Simulate Tampering" before sending
   - Message should fail authentication
   - Console shows "Authentication Tag Mismatch"

3. **Replay Protection:**
   - Check "Simulate Replay Attack"
   - System rejects duplicate sequence numbers
   - Logs show "Replay Attack Detected"

4. **Signature Verification:**
   - Test with invalid signature
   - System rejects unsigned messages
   - Verification failure is logged

---

## Project Structure

```
PQC-Secure-Communication-/
├── app/                           # Main Flask application
│   ├── __init__.py               # App factory
│   ├── config.py                 # Configuration settings
│   ├── models.py                 # Database models
│   ├── auth/                     # Authentication module
│   │   ├── routes.py            # Login, register, logout
│   │   └── __init__.py
│   ├── chat/                     # Real-time chat module
│   │   ├── events.py            # WebSocket event handlers
│   │   └── __init__.py
│   ├── crypto/                   # Cryptography implementations
│   │   ├── classical.py         # Classical crypto functions
│   │   ├── pqc.py               # Post-quantum functions
│   │   ├── hybrid.py            # Hybrid key exchange
│   │   ├── symmetric.py         # AES-256-GCM, ChaCha20
│   │   ├── key_derivation.py    # HKDF, salt generation
│   │   └── x25519_curve.py      # X25519 elliptic curve
│   ├── mail/                     # Email encryption module
│   │   └── mail_routes.py
│   ├── files/                    # File vault module
│   │   └── file_routes.py
│   ├── keys/                     # Key management
│   │   └── key_routes.py
│   ├── api/                      # REST API endpoints
│   │   └── routes.py
│   ├── audit/                    # Audit logging
│   │   └── audit_routes.py
│   ├── static/                   # Frontend assets
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── quantum_flow.css
│   │   └── js/
│   │       ├── app.js           # Core functionality
│   │       └── quantum_flow.js  # UI animations
│   └── templates/                # HTML templates
│       └── index.html            # Main interface
├── tests/                         # Test suite
│   ├── test_crypto.py
│   ├── test_chat_advanced_features.py
│   ├── test_integration.py
│   ├── test_real_crypto_attacks.py
│   └── test_group_and_delete.py
├── instance/                      # Runtime data
│   ├── uploads/                  # Encrypted uploads
│   └── temp_downloads/           # Temporary files
├── requirements.txt              # Python dependencies
├── run.py                        # Application entry point
├── README.md                     # This file
└── DEEP_ARCHITECTURE_ANALYSIS.md # Detailed architecture doc
```

---

## Technical Stack

### Backend:
- **Framework:** Flask 3.0+
- **Python Version:** 3.10 - 3.13
- **Cryptography Library:** liboqs (Open Quantum Safe)
- **Encryption:** cryptography, PyCryptodome
- **Database:** SQLite with SQLAlchemy ORM
- **Session Management:** Flask-Session
- **Real-Time Communication:** Flask-SocketIO, python-socketio

### Frontend:
- **Markup:** HTML5
- **Styling:** CSS3 with custom animations
- **Scripting:** Vanilla JavaScript (ES6+)
- **Real-Time:** Socket.IO client library
- **UI Patterns:** Single Page Application (SPA)

### Security Libraries:
- **liboqs-python:** NIST PQC algorithms
- **cryptography:** HKDF, SHA-3, HMAC
- **Argon2:** Password hashing
- **secrets:** Cryptographically secure random generation

### Development Tools:
- **Testing:** pytest, pytest-cov
- **Linting:** flake8 (optional)
- **Version Control:** Git

---

## How It Works: Message Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURE MESSAGE EXCHANGE                       │
├─────────────────────────────────────────────────────────────────┤

1. HANDSHAKE (Establish Shared Secret)
   ┌──────────────────────────────────────────────────────────┐
   │ Alice                              │                Bob   │
   │ │                                  │                │     │
   │ ├─ Generate ML-KEM-768 keypair     │                │     │
   │ ├─ Generate X25519 keypair         │                │     │
   │ ├─ Send public keys ──────────────────────────────────> │
   │ │                                  │ ← Receive keys │     │
   │ │                                  │ ├─ Generate keys    │
   │ │                                  │ ├─ Compute secret   │
   │ │                    Receive secret < ────────────────  │
   │ └─ Compute same secret             │                │     │
   │    (Both have same 256-bit key!)   │                │     │
   └──────────────────────────────────────────────────────────┘

2. MESSAGE ENCRYPTION
   ┌──────────────────────────────────────────────────────────┐
   │ Alice                                                     │
   │ ├─ Message: "Hello Bob"                                 │
   │ ├─ Encrypt with AES-256-GCM + Shared Key               │
   │ │  Result: Ciphertext + 16-byte Auth Tag               │
   │ ├─ Sign with ML-DSA-65 Private Key                     │
   │ │  Result: Unforgeable Quantum Signature               │
   │ └─ Send: [Ciphertext, Tag, Signature]                  │
   └──────────────────────────────────────────────────────────┘

3. MESSAGE VERIFICATION & DECRYPTION
   ┌──────────────────────────────────────────────────────────┐
   │ Bob                                                       │
   │ ├─ Receive: [Ciphertext, Tag, Signature]               │
   │ ├─ Verify ML-DSA-65 Signature with Alice's Public Key  │
   │ │  ✅ Confirmed: It's really from Alice!               │
   │ ├─ Verify AES-256-GCM Auth Tag                         │
   │ │  ✅ Confirmed: No tampering detected!                │
   │ ├─ Decrypt with Shared Secret Key                      │
   │ │  Result: "Hello Bob"                                 │
   │ └─ Message authenticated & decrypted successfully      │
   └──────────────────────────────────────────────────────────┘
```

---

## Configuration

Edit `app/config.py` to customize:

```python
# Security Settings
SECRET_KEY = os.urandom(32)          # Session encryption key
MAX_MESSAGE_SIZE = 1024 * 1024       # 1MB message limit
SESSION_TIMEOUT = 3600               # 1 hour session timeout

# Cryptography
PQC_ALGORITHM = 'ML-KEM-768'         # Key exchange algorithm
SIGNATURE_ALGORITHM = 'ML-DSA-65'    # Signature algorithm
ENCRYPTION_ALGORITHM = 'AES-256-GCM' # Symmetric encryption

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///secure_comm.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask Settings
DEBUG = False                         # Disable in production
TESTING = False
MAX_CONTENT_LENGTH = 50 * 1024 * 1024 # 50MB file upload limit
```

---

## Troubleshooting

### Issue: "liboqs not found"
```bash
# Solution: Reinstall dependencies
pip install --upgrade --force-reinstall requirements.txt
```

### Issue: Port 5000 already in use
```bash
# Solution: Use different port
python run.py --port 5001
```

### Issue: Database locked
```bash
# Solution: Remove old database
del instance\secure_comm.db
# Restart application
python run.py
```

### Issue: SSL/Certificate errors
```bash
# Enable development mode (local testing only)
export FLASK_ENV=development
python run.py
```

---

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## Security Notice

⚠️ **This is an educational/demonstration project.**

For production use:
- ✅ Enable HTTPS/TLS with valid certificates
- ✅ Use a production WSGI server (Gunicorn, uWSGI)
- ✅ Deploy behind a reverse proxy (Nginx, Apache)
- ✅ Use a production database (PostgreSQL, MySQL)
- ✅ Implement rate limiting and DDoS protection
- ✅ Regular security audits and penetration testing
- ✅ Keep dependencies updated regularly

---

## References & Standards

- **NIST Post-Quantum Cryptography:**
  - FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism
  - FIPS 204: Module-Lattice-Based Digital Signature Standard
  - FIPS 205: Stateless Hash-Based Digital Signature Standard

- **Open Quantum Safe Project:**
  - https://openquantumsafe.org/
  - liboqs: Reference implementation of PQC algorithms

- **Key Standards:**
  - RFC 5869: HKDF (HMAC-based Extract-and-Expand Key Derivation)
  - NIST SP 800-38D: GCTR Mode
  - FIPS 197: AES Specification

---

## License

This project is licensed under the **MIT License** - see the LICENSE.txt file for details.

---

<div align="center">

### Made with ❤️ for Quantum-Safe Communications

**Last Updated:** September 2, 2026  
**Version:** 1.0.0  
**Status:** Production-Ready Demo

[⬆ Back to Top](#-pqc-secure-communication---post-quantum-cryptography-platform)

</div>
