"""
Offline Notes Locker

Created a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

The program:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood)
3. Store all the encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

"""
import os
import json
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)

    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()

    return Fernet(key)


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_vault(data):
    with open(VAULT_FILE, 'w', encoding='utf-8') as f:
        json.dumps(data, f, indent=2)


def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encrypted_content = Fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append(
        {
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
        }
    )

    save_vault(data)
    print("✅ data saved")


def list_notes():
    data = load_vault()

def main():
    load_or_create_key()

if __name__ == "__main__":
    main()