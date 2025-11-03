# Program 8: Keyword Cipher
def keyword_cipher():
    print("=== Keyword Cipher ===")
    keyword = input("Enter keyword: ").upper()
    text = input("Enter plaintext: ").upper()
    
    # Create cipher alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = ''.join(dict.fromkeys(keyword))
    cipher_alpha = keyword + ''.join(c for c in alphabet if c not in keyword)
    
    print(f"\nPlain:  {alphabet}")
    print(f"Cipher: {cipher_alpha}")
    
    # Encrypt
    result = ""
    for char in text:
        if char in alphabet:
            result += cipher_alpha[alphabet.index(char)]
        else:
            result += char
    
    print(f"\nEncrypted: {result}")

if __name__ == "__main__":
    keyword_cipher()