# Program 40: Frequency Attack Mono (Duplicate)
# Same as Programs 16 and 37
def frequency_attack_mono():
    print("=== Frequency Attack on Monoalphabetic Cipher ===")
    ciphertext = input("Enter ciphertext: ").upper()
    
    freq = {}
    for char in ciphertext:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    mapping = {}
    for i, (cipher_char, count) in enumerate(sorted_freq):
        if i < len(english_freq):
            mapping[cipher_char] = english_freq[i]
    
    decrypted = ''.join(mapping.get(c, c) for c in ciphertext)
    
    print(f"\nTop 10 frequency mappings:")
    for i, (c, p) in enumerate(list(mapping.items())[:10]):
        print(f"{c} → {p}")
    
    print(f"\nDecrypted text (top 1 result):")
    print(decrypted)

if __name__ == "__main__":
    frequency_attack_mono()