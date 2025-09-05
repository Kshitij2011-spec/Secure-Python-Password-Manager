import os
import base64
import getpass

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


def derive_key(master_pwd: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    key = kdf.derive(master_pwd.encode())
    return base64.urlsafe_b64encode(key)


def load_or_create_salt() -> bytes:
    if not os.path.exists("salt.bin"):
        with open("salt.bin", "wb") as f:
            f.write(os.urandom(16))
    with open("salt.bin", "rb") as f:
        return f.read()


def view(fer):
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, pwd = data.split("|")
                try:
                    print(f"User: {user} | Password: {fer.decrypt(pwd.encode()).decode()}")
                except:
                    print(f"User: {user} | [Decryption failed]")


def add(fer):
    name = input("Enter account name: ")
    pwd = input("Enter account password: ")
    enc_pwd = fer.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + enc_pwd + "\n")
    print("Password saved!")


def main():
    print("=== Secure Password Manager ===")
    master_pwd = input("Enter your master password: ")

    salt = load_or_create_salt()
    key = derive_key(master_pwd, salt)
    fer = Fernet(key)

    while True:
        print("\nSelect mode:")
        print("1. View passwords")
        print("2. Add new password")
        print("3. Quit")
        mode = input("Choice (1/2/3): ").strip()

        if mode == "1":
            view(fer)
        elif mode == "2":
            add(fer)
        elif mode == "3":
            print("Exiting. Bye 👋")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
