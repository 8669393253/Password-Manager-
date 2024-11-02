from cryptography.fernet import Fernet
import json
import os
import re
import getpass

def generate_key():
    return Fernet.generate_key()

def load_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_password(password):
    f = Fernet(load_key())
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    f = Fernet(load_key())
    return f.decrypt(encrypted_password).decode()

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return {}

def is_strong_password(password):
    return (len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

def main():
    passwords = load_passwords()
    
    while True:
        action = input("Choose an action: add, retrieve, delete, or exit: ").strip().lower()

        if action == "add":
            site = input("Enter the site name: ")
            password = getpass.getpass("Enter the password: ")  # Hide input

            if is_strong_password(password):
                encrypted_password = encrypt_password(password)
                passwords[site] = encrypted_password.decode()
                save_passwords(passwords)
                print(f"Password for {site} added.")
            else:
                print("Password is not strong enough. Please try again.")

        elif action == "retrieve":
            site = input("Enter the site name: ")
            if site in passwords:
                decrypted_password = decrypt_password(passwords[site].encode())
                print(f"Password for {site}: {decrypted_password}")
            else:
                print("No password found for that site.")

        elif action == "delete":
            site = input("Enter the site name: ")
            if site in passwords:
                del passwords[site]
                save_passwords(passwords)
                print(f"Password for {site} deleted.")
            else:
                print("No password found for that site.")

        elif action == "exit":
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == 'yes':
                break

        else:
            print("Invalid action. Please choose add, retrieve, delete, or exit.")

if __name__ == "__main__":
    main()
