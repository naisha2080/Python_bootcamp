"""
Docstring for Python_Utilities.Caesar_Cipher

Create a Python script that helps you send secret message to your friend using simple encryption.

Ask the user if they want to encrypt or decrypt a message.
If encrypt:
- Ask for a message and a numeric sceret key
- Use a Caesar Cipher (shift letters by the key value).
- Output the encrypted message.
If decrypt:
- Ask for the encrypted message and key
- Reverse the encryption to get the original message.

letter → number → shift → wrap → letter again
"""
def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
    else:
        result += char #if not an alphabet, we'll simply add it to the result.
    return result


def decrypt(message, key):
    return encrypt(message, -key)


print("Secret message program")
choice = input("Do you want to E(Encrypt) or D(Decrypt) ?").strip().lower()

if choice == "e":
    text = input("Enter your encrypted message: \n")
    try:
        key = int(input("Enter a number between 1-26 "))
        encrypted = encrypt(text, key)
        print(encrypted)
    except ValueError:
        print("Choose a valid key")
elif choice == "d":
    text = input("Enter your decrypted message: \n")
    try:
        key = int(input("Enter a number between 1-26 "))
        decrypted = decrypt(text, key)
        print(decrypted)
    except ValueError:
        print("Choose a valid key")
else:
    print("Invalid choice")