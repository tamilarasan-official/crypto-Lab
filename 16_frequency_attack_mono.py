# Program 16: Frequency Attack on Monoalphabetic
def frequency_attack_mono():
    print("=== Frequency Attack on Monoalphabetic Cipher ===")
    ciphertext = input("Enter ciphertext: ").upper()
    
    # Calculate frequency
    freq = {}
    for char in ciphertext:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # English letter frequency
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    # Create mapping
    mapping = {}
    for i, (cipher_char, _) in enumerate(sorted_freq):
        if i < len(english_freq):
            mapping[cipher_char] = english_freq[i]
    
    # Decrypt
    decrypted = ""
    for char in ciphertext:
        if char in mapping:
            decrypted += mapping[char]
        else:
            decrypted += char
    
    print("\nFrequency analysis mapping:")
    for cipher, plain in list(mapping.items())[:10]:
        print(f"{cipher} → {plain}")
    
    print(f"\nDecrypted text:\n{decrypted}")

if __name__ == "__main__":
    frequency_attack_mono()