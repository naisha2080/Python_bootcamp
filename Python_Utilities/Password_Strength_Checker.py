"""
Password Strength Checker & Suggestion Tool

Build a python script that checks thr strength of a password based on:
1. At least 8 characters
2. At least one uppercase
3. At least one lower case
4. At least one digit
5. At least one special character

Suggest a strong password if the password is too weak
"""
import string
from prompt_toolkit import prompt
import random

def password_strength_checker(password):
    issues = []
    if len(password) < 8 :
        issues.append("Should have at least 8 characters")
    if not any(c.islower() for c in password):
        issues.append("Should have at least one lower character")
    if not any(c.isupper() for c in password):
        issues.append("Should have at least one upper character")
    if not any(c.isdigit() for c in password):
        issues.append("Should have at least one number")
    if not any(c in string.punctuation for c in password):
        issues.append("Should have at least one special character")
    return issues

def generate_strong_password(length=12):
    char = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(char) for _ in range (length))

suggestion = generate_strong_password()

#for masking the password here
password = prompt("Enter your password: ", is_password=True)
issues = password_strength_checker(password)

if not issues: 
    print(f"Strong Password")
else:
    print(f"Weak Password")
    for issue in issues:
        print(f"- {issue}")
    print(f"\nSuggested Password: {suggestion}\n")


