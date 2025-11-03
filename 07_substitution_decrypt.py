# Program 7: Simple Substitution Decryption
def frequency_analysis(ciphertext):
    freq = {}
    for char in ciphertext.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

def main():
    print("=== Substitution Cipher Decryption ===")
    ciphertext = input("Enter ciphertext: ")
    
    print("\nFrequency Analysis:")
    freq = frequency_analysis(ciphertext)
    for char, count in freq[:10]:
        print(f"{char}: {count}")
    
    print("\nHints:")
    print("- Most common English letter: E")
    print("- Common word: THE")
    print("- Look for repeated patterns")
    
    mapping = {}
    while True:
        cipher_char = input("\nCipher char (or 'done'): ").upper()
        if cipher_char == 'DONE':
            break
        plain_char = input("Maps to: ").upper()
        mapping[cipher_char] = plain_char
    
    decrypted = ''.join(mapping.get(c, c) for c in ciphertext.upper())
    print(f"\nDecrypted: {decrypted}")

if __name__ == "__main__":
    main()