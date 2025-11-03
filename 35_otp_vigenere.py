# Program 35: One-Time Pad Vigenere
def otp_vigenere():
    print("=== One-Time Pad (Vigenere Variant) ===")
    
    plaintext = input("Enter plaintext: ").lower().replace(" ", "")
    key_stream_input = input("Enter key stream (space-separated numbers 0-25): ")
    key_stream = list(map(int, key_stream_input.split()))
    
    if len(key_stream) < len(plaintext):
        print("Error: Key stream too short!")
        return
    
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            encrypted = (ord(plaintext[i]) - 97 + key_stream[i]) % 26
            ciphertext += chr(encrypted + 97)
        else:
            ciphertext += plaintext[i]
    
    print(f"\nPlaintext:  {plaintext}")
    print(f"Key stream: {key_stream[:len(plaintext)]}")
    print(f"Ciphertext: {ciphertext}")
    
    print("\nDecryption:")
    decrypted = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            decrypted_char = (ord(ciphertext[i]) - 97 - key_stream[i]) % 26
            decrypted += chr(decrypted_char + 97)
        else:
            decrypted += ciphertext[i]
    
    print(f"Decrypted:  {decrypted}")

if __name__ == "__main__":
    otp_vigenere()