# Task 9: Custom Encryption-Decryption (Caesar Cipher Example)
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = input("Enter message: ")
key = int(input("Enter shift key: "))

encrypted = encrypt(msg, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
