# Password Manager

A simple and secure password manager that allows users to add, retrieve, and delete passwords. The application encrypts passwords for security and stores them in a JSON file.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Security](#security)
- [License](#license)

## Features
- **Password Encryption**: All passwords are securely encrypted using the Fernet symmetric encryption method.
- **Strong Password Validation**: Ensures that passwords meet complexity requirements (length, character types).
- **Data Storage**: Stores encrypted passwords in a JSON file.
- **User-Friendly Interface**: Simple command-line interface for interacting with the password manager.

## Requirements
- Python 3.x
- cryptography library (for password encryption)

### Install the Required Library
To install the cryptography library, run:
pip install cryptography

## Installation
1. Clone the repository or download the script.
2. Navigate to the directory where the script is located.
3. Run the script using Python:
4. 
   python password_manager.py

## Usage
Upon running the script, you will be prompted to choose an action:
- **add**: Add a new password for a specific site.
- **retrieve**: Retrieve the password for a specific site.
- **delete**: Delete the password for a specific site.
- **exit**: Exit the application.

### Example
1. To add a password, choose add, enter the site name, and type the password (input will be hidden).
2. To retrieve a password, choose retrieve and provide the site name.
3. To delete a password, choose delete and confirm the site name.

## Functionality
### Key Functions
- generate_key(): Generates a new encryption key.
- load_key(): Loads the encryption key from a file, or generates a new one if it doesn’t exist.
- encrypt_password(password): Encrypts a given password using the loaded key.
- decrypt_password(encrypted_password): Decrypts an encrypted password.
- save_passwords(passwords): Saves the dictionary of passwords to a JSON file.
- load_passwords(): Loads passwords from the JSON file.
- is_strong_password(password): Validates the strength of the provided password based on defined criteria.

## Security
- Passwords are stored in an encrypted format, ensuring that even if the storage file is accessed, the actual passwords remain secure.
- The password manager validates passwords against common criteria, promoting the use of strong passwords to enhance security.

### Important Notes
- Always ensure you back up your passwords.json and key.key files to prevent data loss.
- Do not share your encryption key (key.key) as it is essential for decrypting your stored passwords.

## License
This project is licensed under the MIT License. Feel free to modify and use it as needed.
