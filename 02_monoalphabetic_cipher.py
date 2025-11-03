# Program 2: Monoalphabetic Substitution Cipher
def monoalphabetic_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    result = ""
    for char in plaintext:
        if char in alphabet:
            result += key[alphabet.index(char)]
        else:
            result += char
    return result

def monoalphabetic_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()
    result = ""
    for char in ciphertext:
        if char in key:
            result += alphabet[key.index(char)]
        else:
            result += char
    return result

def main():
    print("=== Monoalphabetic Cipher ===")
    choice = input("'e' for encrypt, 'd' for decrypt: ").lower()
    text = input("Enter text: ")
    key = input("Enter 26-letter key: ").upper()
    
    if choice == 'e':
        print(f"Encrypted: {monoalphabetic_encrypt(text, key)}")
    else:
        print(f"Decrypted: {monoalphabetic_decrypt(text, key)}")

if __name__ == "__main__":
    main()