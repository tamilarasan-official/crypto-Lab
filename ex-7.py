# Simple Substitution Cipher Breaker

def frequency_analysis(text):
    """Count frequency of each character."""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

def substitute(text, mapping):
    """Apply substitution mapping to text."""
    result = ""
    for char in text:
        result += mapping.get(char, char)
    return result

# Ciphertext
ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?"""

print("SUBSTITUTION CIPHER BREAKER")
print("=" * 60)
print("\nCiphertext:")
print(ciphertext)
print()

# Frequency analysis
freq = frequency_analysis(ciphertext)
print("Character Frequencies:")
for char, count in freq[:15]:
    print(f"  '{char}': {count}")
print()

# English letter frequencies (most common)
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# Create initial mapping based on frequency
mapping = {}
print("Initial frequency-based mapping:")
for i, (char, count) in enumerate(freq[:15]):
    if i < len(english_freq):
        mapping[char] = english_freq[i].lower()
        print(f"  '{char}' → '{english_freq[i].lower()}'")
print()

# Decrypt with initial mapping
decrypted = substitute(ciphertext, mapping)
print("Initial Decryption:")
print(decrypted)
print()

# Manual substitution refinement
print("=" * 60)
print("MANUAL REFINEMENT")
print("=" * 60)
print("\nRefine the mapping by substituting characters:")
print("Enter mappings like: 8 = a  (means replace '8' with 'a')")
print("Type 'done' to finish, 'show' to see current result")
print()

while True:
    user_input = input("Mapping (or 'done'/'show'): ").strip()
    
    if user_input.lower() == 'done':
        break
    elif user_input.lower() == 'show':
        print("\nCurrent decryption:")
        print(substitute(ciphertext, mapping))
        print()
        continue
    
    # Parse input like "8 = a" or "8=a"
    if '=' in user_input:
        parts = user_input.split('=')
        if len(parts) == 2:
            cipher_char = parts[0].strip()
            plain_char = parts[1].strip().lower()
            mapping[cipher_char] = plain_char
            print(f"  Updated: '{cipher_char}' → '{plain_char}'")
            print(f"  Preview: {substitute(ciphertext[:50], mapping)}...")
        else:
            print("  Invalid format. Use: 8 = a")
    else:
        print("  Invalid format. Use: 8 = a")

# Final result
print("\n" + "=" * 60)
print("FINAL DECRYPTION")
print("=" * 60)
print(substitute(ciphertext, mapping))
print()

# Show final mapping
print("\nFinal Mapping Used:")
for cipher, plain in sorted(mapping.items()):
    print(f"  '{cipher}' → '{plain}'")