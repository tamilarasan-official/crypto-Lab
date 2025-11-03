# Program 4: Vigenere (Polyalphabetic) Cipher
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def main():
    print("=== Vigenere Cipher ===")
    choice = input("'e' for encrypt, 'd' for decrypt: ").lower()
    text = input("Enter text: ")
    key = input("Enter key: ")
    
    if choice == 'e':
        print(f"Encrypted: {vigenere_encrypt(text, key)}")
    else:
        print(f"Decrypted: {vigenere_decrypt(text, key)}")

if __name__ == "__main__":
    main()