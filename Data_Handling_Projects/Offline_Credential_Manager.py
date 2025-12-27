"""
Docstring for Data_Handling_Projects.Offline_Credential_Manager

Created a CLI tool to manage login credentials (website, username, password) in  an encoded local file (`vault.txt`).

This program :
1. Add new credentials (website, username, password)
2. Automatically rate password strength - weak, medium, strong
3. Encode the saved content using Base64
4. View all saved credentials (decoding them)
5. Update password for any existing entry (assignment)

"""
import base64
import os
import string

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    issues = []
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!.,;@#$%^&*" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
   
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]


def add_credentials():
    website = input("Website: ").strip()
    username = input("Usernaame: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)

    line = f"{website} | {username} | {password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding='utf-8') as f:
        f.write(encoded_line + "\n")
        
    print(f"{strength}")
    print("✅ Credential saved")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found❌")
        return
    
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split(" | ")
            hidden_password = '*' * len(password)
            print(f"{website} | {username} | {password}")
            

def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credential")
        print("3. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1": add_credentials()
            case "2": view_credentials()
            case "3": break
            case _: print("Invalid Choice")

if __name__ == "__main__":
    main()