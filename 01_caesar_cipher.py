# Program 1: Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Enter 'e' for encrypt or 'd' for decrypt: ").lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift value (1-25): "))
    
    if choice == 'e':
        print(f"Encrypted: {caesar_encrypt(text, shift)}")
    elif choice == 'd':
        print(f"Decrypted: {caesar_decrypt(text, shift)}")

if __name__ == "__main__":
    main()