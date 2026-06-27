# Cryptography Basics: Symmetric Encryption & Ransomware Simulation

## 📝 Description
This educational security tool demonstrates the mathematical principles of symmetric key cryptography. Using the standard `cryptography.fernet` implementation, the application simulates a controlled ransomware event by generating an encryption key, transforming a plaintext asset into unreadable ciphertext, and subsequently executing an authorized cryptographic recovery phase to restore the file to its original state.

## 🛠️ Features
* **Symmetric Key Generation:** Implements secure key generation vectors via the AES-based Fernet spec.
* **Controlled Data Masking:** Dynamically locks targeted files while preserving resource integrity.
* **Automated Data Recovery:** Demonstrates the exact reversible mechanics utilized by standard decryption engines during incident response.

## 🚀 How to Run It

### Prerequisites
* Python 3.x installed.
* Python `cryptography` package installed (`pip3 install cryptography`).

### Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/crypto-ransomware-simulator.git](https://github.com/YOUR-USERNAME/crypto-ransomware-simulator.git)
