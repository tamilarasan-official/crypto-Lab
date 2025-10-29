# Polyalphabetic Substitution Cipher (Vigenère Cipher)

def generate_key(plaintext, keyword):
    """
    Generate a key that matches the length of the plaintext.
    The keyword is repeated cyclically to match plaintext length.
    """
    keyword = keyword.upper()
    plaintext = ''.join(filter(str.isalpha, plaintext.upper()))
    
    # Repeat keyword to match plaintext length
    key = ""
    keyword_index = 0
    
    for i in range(len(plaintext)):
        key += keyword[keyword_index % len(keyword)]
        keyword_index += 1
    
    return key


def encrypt_polyalphabetic(plaintext, keyword):
    """
    Encrypt plaintext using polyalphabetic substitution cipher.
    Each letter uses a different Caesar cipher shift based on the keyword.
    """
    ciphertext = ""
    keyword = keyword.upper()
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.upper()
            
            # Get the shift value from keyword (A=0, B=1, ..., Z=25)
            shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            
            # Apply Caesar cipher with the shift
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            
            # Preserve original case
            if not is_upper:
                encrypted_char = encrypted_char.lower()
            
            ciphertext += encrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    
    return ciphertext


def decrypt_polyalphabetic(ciphertext, keyword):
    """
    Decrypt ciphertext using polyalphabetic substitution cipher.
    Each letter uses a different Caesar cipher shift based on the keyword.
    """
    plaintext = ""
    keyword = keyword.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.upper()
            
            # Get the shift value from keyword (A=0, B=1, ..., Z=25)
            shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            
            # Apply reverse Caesar cipher with the shift
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            
            # Preserve original case
            if not is_upper:
                decrypted_char = decrypted_char.lower()
            
            plaintext += decrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char
    
    return plaintext


def display_encryption_table(plaintext, keyword):
    """
    Display a detailed table showing how each letter is encrypted.
    """
    plaintext_letters = ''.join(filter(str.isalpha, plaintext.upper()))
    key = generate_key(plaintext, keyword)
    
    print("\nEncryption Details:")
    print("-" * 70)
    print(f"{'Position':<10} {'Plaintext':<12} {'Key Letter':<12} {'Shift':<8} {'Ciphertext':<12}")
    print("-" * 70)
    
    for i in range(min(len(plaintext_letters), 20)):  # Show first 20 letters
        plain_char = plaintext_letters[i]
        key_char = key[i]
        shift = ord(key_char) - ord('A')
        cipher_char = chr((ord(plain_char) - ord('A') + shift) % 26 + ord('A'))
        
        print(f"{i+1:<10} {plain_char:<12} {key_char:<12} {shift:<8} {cipher_char:<12}")
    
    if len(plaintext_letters) > 20:
        print(f"... (showing first 20 of {len(plaintext_letters)} letters)")
    print("-" * 70)


def display_vigenere_square():
    """
    Display the Vigenère square (tabula recta) - first 10x10 section.
    """
    print("\nVigenère Square (first 10x10 section):")
    print("  ", end="")
    for i in range(10):
        print(f" {chr(65+i)}", end="")
    print()
    
    for i in range(10):
        print(f"{chr(65+i)} ", end="")
        for j in range(10):
            print(f" {chr(65 + (i+j) % 26)}", end="")
        print()
    print()


# Main Program
print("=" * 70)
print("POLYALPHABETIC SUBSTITUTION CIPHER (VIGENÈRE CIPHER)")
print("=" * 70)
print()
print("This cipher uses multiple Caesar ciphers based on a keyword.")
print("Each letter of the keyword determines a different shift value.")
print()

# Display Vigenère square
display_vigenere_square()

# Get keyword from user
keyword = input("Enter the keyword: ")

# Get plaintext from user
plaintext = input("Enter the plaintext message: ")
print()

# Generate the repeating key
full_key = generate_key(plaintext, keyword)
plaintext_letters = ''.join(filter(str.isalpha, plaintext.upper()))

print(f"Keyword: {keyword.upper()}")
print(f"Plaintext (letters only): {plaintext_letters}")
print(f"Repeated key: {full_key}")
print()

# Display encryption table
display_encryption_table(plaintext, keyword)
print()

# Encrypt the message
ciphertext = encrypt_polyalphabetic(plaintext, keyword)

# Display results
print("=" * 70)
print("RESULTS:")
print("=" * 70)
print(f"Original Plaintext:   {plaintext}")
print(f"Keyword:              {keyword.upper()}")
print(f"Encrypted Ciphertext: {ciphertext}")
print()

# Decrypt to verify
decrypted = decrypt_polyalphabetic(ciphertext, keyword)
print(f"Decrypted Plaintext:  {decrypted}")
print("=" * 70)
print()

# Additional example
print("=" * 70)
print("EXAMPLE: Encrypting 'HELLO WORLD' with keyword 'KEY'")
print("=" * 70)

example_plain = "HELLO WORLD"
example_key = "KEY"

example_cipher = encrypt_polyalphabetic(example_plain, example_key)

print(f"\nPlaintext: {example_plain}")
print(f"Keyword:   {example_key}")
print()

# Show letter-by-letter encryption
example_letters = ''.join(filter(str.isalpha, example_plain.upper()))
repeated_key = generate_key(example_plain, example_key)

print("Letter-by-letter encryption:")
for i in range(len(example_letters)):
    plain_char = example_letters[i]
    key_char = repeated_key[i]
    shift = ord(key_char) - ord('A')
    cipher_char = chr((ord(plain_char) - ord('A') + shift) % 26 + ord('A'))
    print(f"  {plain_char} + {key_char}(shift={shift:2d}) = {cipher_char}")

print(f"\nCiphertext: {example_cipher}")
print()

example_decrypt = decrypt_polyalphabetic(example_cipher, example_key)
print(f"Decrypted:  {example_decrypt}")
print()

print("=" * 70)
print("SUMMARY:")
print("=" * 70)
print("The polyalphabetic substitution cipher uses a keyword to")
print("determine multiple Caesar cipher shifts. Each letter in the")
print("plaintext is encrypted using a different monoalphabetic cipher")
print("based on the corresponding letter in the repeated keyword.")
print()
print("Formula: C[i] = (P[i] + K[i]) mod 26")
print("Where P = Plaintext, K = Key, C = Ciphertext")
print("=" * 70)