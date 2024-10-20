# Password-Manager
You can store, retrieve or even delete your password for multiple sites.
Password Manager
A command-line password manager that securely stores, retrieves, and manages your passwords using strong encryption. This application ensures your sensitive information is safe while providing an easy-to-use interface for everyday password management.
Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Security Considerations](#security-considerations)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
Features
- Secure Password Storage: Encrypts passwords using the Fernet symmetric encryption algorithm, ensuring that your passwords are not stored in plain text.
- Password Strength Validation: Checks for strong passwords based on defined criteria, such as length and character variety (uppercase, lowercase, digits, and special characters).
- Telegram Notifications: Sends real-time notifications to a specified Telegram chat when passwords are added or deleted, allowing for easy monitoring of password management activities.
- User-Friendly Interface: Provides a simple command-line interface to facilitate easy interaction for adding, retrieving, and deleting passwords.

Requirements
- Python 3.x
- `cryptography` library
- `requests` library

You can install the required libraries using pip: pip install cryptography requests
Installation
1. Clone the Repository:
   git clone <repository_url>
   cd password-manager

2. Set Up Environment Variables:  
To enable Telegram notifications, you need to provide your Telegram bot token and chat ID as environment variables. You can do this by creating a `.env` file or exporting them in your terminal:
   export BOT_TOKEN=your_telegram_bot_token
   export CHAT_ID=your_telegram_chat_id
3. Run the Application:
   Start the password manager by running the following command: python password_manager.py
Usage
Upon running the script, you'll be presented with the following options:
1. Add: 
   - Prompted to enter a site name and a password.
   - The password will be validated for strength before being encrypted and stored.

2. Retrieve:
   - Enter the site name to retrieve the corresponding encrypted password, which will be decrypted and displayed.

3. Delete:
   - Provide the site name to delete the corresponding password from storage.

4. Exit:
   - Confirm to exit the application.

Example Commands

- To add a password:
  - When prompted, input the site name (e.g., "GitHub") and the password.
  
- To retrieve a password:
  - Input the site name (e.g., "GitHub") to see the decrypted password.

- To delete a password:
  - Enter the site name (e.g., "GitHub") to remove the password from storage.

Security Considerations

- Encryption: All passwords are encrypted before being stored, using a strong encryption standard (Fernet).
- Key Management: The encryption key is stored in `key.key`. Ensure that this file is kept secure and not shared.
- File Permissions: Set appropriate permissions on `key.key` and `passwords.json` to limit access to unauthorized users. You can use commands like `chmod 600 key.key passwords.json` on Unix-based systems.

Environment Variables
The following environment variables are required for Telegram notifications:
- BOT_TOKEN: Your Telegram bot token, which can be obtained by creating a new bot via the BotFather.
- CHAT_ID: The unique identifier for the chat where you want to receive notifications. You can obtain this by sending a message to your bot and checking the updates.
Contributing
Contributions are welcome! If you have suggestions for improvements or features, please fork the repository and submit a pull request. Make sure to adhere to the following guidelines:
- Follow the code style used in the project.
- Write clear commit messages.
- Test your changes before submitting.
Acknowledgements
- [Cryptography](https://cryptography.io/) for providing the encryption framework.
- [Telegram Bot API](https://core.telegram.org/bots/api) for the messaging functionality.
