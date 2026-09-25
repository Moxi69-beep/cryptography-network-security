import argparse
import hashlib
import os
from cryptography.fernet import Fernet


def generate_key(key_file="secret.key"):
    """Generates a key and saves it locally (keeps key out of repository)."""
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
    print(f"[+] Key generated and saved to '{key_file}'")


def load_key(key_file="secret.key"):
    if not os.path.exists(key_file):
        raise FileNotFoundError(
            f"[-] Key file '{key_file}' not found. Run --action genkey first!"
        )
    with open(key_file, "rb") as f:
        return f.read()


def encrypt_file(input_file, output_file, key_file="secret.key"):
    """a. Encrypts student record file."""
    try:
        key = load_key(key_file)
        f = Fernet(key)
        with open(input_file, "rb") as file:
            data = file.read()
        encrypted_data = f.encrypt(data)
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
        print(f"[+] Successfully encrypted '{input_file}' -> '{output_file}'")
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
    except Exception as e:
        print(f"[-] Encryption failed: {e}")


def decrypt_file(input_file, output_file, key_file="secret.key"):
    """b. Decrypts file and restores original contents."""
    try:
        key = load_key(key_file)
        f = Fernet(key)
        with open(input_file, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        print(f"[+] Successfully decrypted '{input_file}' -> '{output_file}'")
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
    except Exception as e:
        print(f"[-] Decryption failed (invalid key or file corrupted): {e}")


def calculate_hash(file_path):
    """c. Calculates SHA-256 hash."""
    try:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[-] Error: File '{file_path}' not found.")
        return None


def verify_integrity(file_path, expected_hash):
    """Verifies if file has changed."""
    current_hash = calculate_hash(file_path)
    if current_hash:
        print(f"Current SHA-256 : {current_hash}")
        print(f"Expected SHA-256: {expected_hash}")
        if current_hash.lower() == expected_hash.lower():
            print("[+] Integrity Verified: File has NOT been altered.")
        else:
            print("[!] ALERT: File integrity check failed! File modified.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Security Toolkit for Encryption & Integrity"
    )
    parser.add_argument(
        "--action",
        choices=["genkey", "encrypt", "decrypt", "hash", "verify"],
        required=True,
    )
    parser.add_argument("--file", help="Path to input file")
    parser.add_argument("--out", help="Path to output file")
    parser.add_argument("--key", default="secret.key", help="Key file path")
    parser.add_argument("--hash", help="Expected hash for verification")

    args = parser.parse_args()

    if args.action == "genkey":
        generate_key(args.key)
    elif args.action == "encrypt":
        encrypt_file(args.file, args.out, args.key)
    elif args.action == "decrypt":
        decrypt_file(args.file, args.out, args.key)
    elif args.action == "hash":
        h = calculate_hash(args.file)
        if h:
            print(f"SHA-256 Hash: {h}")
    elif args.action == "verify":
        if not args.hash:
            print("[-] Error: Please provide --hash to verify against.")
        else:
            verify_integrity(args.file, args.hash)