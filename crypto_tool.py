import sys
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("[-] Dependency Error: cryptography library not found.")
    print("[*] Install it later using: pip3 install cryptography")
    sys.exit(1)

TARGET_FILE = "sensitive_data.txt"

def generate_and_save_key():
    """Generates a unique symmetric key and saves it locally."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Loads the secret key from the local directory."""
    return open("secret.key", "rb").read()

print("-" * 55)
print("🔐 CRYPTOGRAPHIC STUDY: SYMMETRIC ENCRYPTION ENGINE 🔐")
print("-" * 55)

# Setup dummy file for analysis
with open(TARGET_FILE, "w") as f:
    f.write("CONFIDENTIAL: Financial reports and employee master credentials.")

print(f"[+] Creating plaintext target asset: {TARGET_FILE}")

# 1. Simulate Symmetric Encryption Phase
key = generate_and_save_key()
fernet = Fernet(key)

with open(TARGET_FILE, "rb") as file:
    original_data = file.read()

encrypted_data = fernet.encrypt(original_data)

with open(TARGET_FILE, "wb") as file:
    file.write(encrypted_data)

print(f"[!] ENCRYPTION COMPLETE: {TARGET_FILE} has been locked.")
print(f"    Ciphertext: {encrypted_data[:40]}...")

# 2. Simulate Decryption Phase
print("\n[*] Initiating Recovery Workflow...")
secret_key = load_key()
recovery_fernet = Fernet(secret_key)

decrypted_data = recovery_fernet.decrypt(encrypted_data)

with open(TARGET_FILE, "wb") as file:
    file.write(decrypted_data)

print(f"✅ DECRYPTION COMPLETE: Data successfully restored to plaintext.")
print(f"    Restored Content: {decrypted_data.decode('utf-8')}")
print("-" * 55)
