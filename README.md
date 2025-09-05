Secure Python Password Manager

A simple command-line password manager in Python that encrypts your passwords using a master password. Uses Fernet symmetric encryption with a strong key derived from your master password.

Features

Add and view passwords securely

Encrypts passwords with a master password

Uses PBKDF2-HMAC-SHA256 key derivation

Easy-to-use CLI interface

Works on Windows, macOS, and Linux

Getting Started
Prerequisites

Python 3.7+ is required. You also need the cryptography library:

pip install cryptography

Usage

Clone or download the repository.

Run the program:

python pw_manager.py


On first run, the program will create a random salt file (salt.bin).

Enter a master password when prompted.

Use the menu to view or add passwords.

Menu Options

1. View passwords – Displays all saved passwords.

2. Add new password – Add a new account with username and password.

3. Quit – Exit the program.

Security Notes

Do not upload passwords.txt or salt.bin to GitHub — these contain your encrypted passwords.

Keep your master password safe. Losing it means losing access to all passwords.

The program stores all passwords locally in an encrypted file.
