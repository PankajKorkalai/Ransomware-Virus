# 🔐 Ransomware (Educational Purpose Only)

## 📖 Overview

This project is a Python-based ransomware developed for **educational purposes only**. It is intended to demonstrate how ransomware works and to educate others about cybersecurity threats. **This software should not be used maliciously.**

## ❗ Important Warning

⚠️ **Do not run the `rw.exe` file located in the `dist` folder.** 

## ✨ Features

- 🔒 **Encryption:** Encrypts files on the victim's machine using a strong encryption algorithm.
- 🔑 **Decryption:** Provides a decryption method to restore the files after payment of the ransom (for educational purposes).
- ⚙️ **Customizable:** Allows modification of the encryption key, target directories, and more.

## 🛠️ How It Works

1. **Encryption:** 
   - The ransomware scans the victim's machine for files of specific types (e.g., `.txt`, `.jpg`, etc.).
   - It encrypts these files using an encryption algorithm (e.g., AES) and appends a specific extension to the file names.

2. **💰 Ransom Note:**
   - After encryption, the ransomware generates a ransom note, usually in the form of a text file, instructing the victim on how to decrypt their files.

3. **🔓 Decryption:**
   - If the ransom is "paid" (in the educational scenario, after understanding the process), the ransomware can decrypt the files using a provided decryption key.

## 🚀 Usage

### 📋 Prerequisites

- 🐍 Python 3.x
- 📦 Required Python libraries (install via `pip`):
