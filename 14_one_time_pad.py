# Program 14: One-Time Pad
def one_time_pad():
    print("=== One-Time Pad ===")
    
    # Part a
    plaintext = "sendmoremoney"
    key_stream = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
    
    ciphertext = ""
    for i in range(len(plaintext)):
        encrypted = (ord(plaintext[i]) - 97 + key_stream[i]) % 26
        ciphertext += chr(encrypted + 97)
    
    print(f"Plaintext: {plaintext}")
    print(f"Key stream: {key_stream}")
    print(f"Ciphertext: {ciphertext}")
    
    # Part b
    target = "cashnotneeded"
    new_key = []
    for i in range(len(target)):
        key_val = (ord(ciphertext[i]) - ord(target[i])) % 26
        new_key.append(key_val)
    
    print(f"\nTo decrypt to '{target}':")
    print(f"New key stream: {new_key}")

if __name__ == "__main__":
    one_time_pad()