# 🔐 Secure Python Password Manager

A simple **command-line password manager** in Python that encrypts your passwords using a **master password**.  
It uses **Fernet symmetric encryption** with a strong key derived from your master password.  

---

## ✨ Features
- 🔒 Add and view passwords securely  
- 🔑 Encrypts passwords with a **master password**  
- 🛡️ Uses **PBKDF2-HMAC-SHA256** key derivation  
- 💻 Easy-to-use CLI interface  
- 🌍 Works on **Windows, macOS, and Linux**

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python **3.7+**  
- Install dependencies:
  pip install cryptography

### ▶️ Usage
1. Clone or download the repository.  
2. Run the program:
python pw_manager.py

- On first run, the program will create a random **salt file** (`salt.bin`).  
- Enter a **master password** when prompted.  
- Use the menu to view or add passwords.  

---

## 📖 Menu Options
1.View passwords – Displays all saved passwords
2.Add new password – Add a new account with username and password
3.Quit – Exit the program

---

## 📝 Example Workflow
Run the program:
=== Secure Password Manager ===
Enter your master password:****

Choose **Add new password**:

Select mode:
1.View passwords
2.Add new password
3.Quit
Choice (1/2/3): 2
Enter account name: Gmail
Enter account password: ****
Password saved!

View stored passwords:

Select mode:
1.View passwords
2.Add new password
3.Quit
Choice (1/2/3): 1
User: Gmail | Password: mysecretpassword

---

## ⚠️ Security Notes
- ❌ Do **not** upload `passwords.txt` or `salt.bin` to GitHub — these contain your encrypted passwords.  
- 🔑 Keep your **master password safe**. Losing it means losing access to all saved passwords.  
- 💾 All passwords are stored **locally** in an encrypted file.  

---

## 🔮 Future Improvements
- 🔀 Add a **random password generator**  
- 📋 Copy passwords to clipboard instead of printing  
- 📝 Add **delete/edit** functions for saved passwords  
- 🖥️ Build a **GUI version**  

--- 


