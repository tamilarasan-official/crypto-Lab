import random

def create_cipher_key():
    """Create a random substitution key"""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def encrypt(text, key):
    """Encrypt text using substitution key"""
    result = ""
    for char in text:
        if char.upper() in key:
            # Replace with cipher letter, keep same case
            new_char = key[char.upper()]
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char  # Keep spaces and punctuation
    return result

def decrypt(text, key):
    """Decrypt text by reversing the key"""
    reverse_key = {v: k for k, v in key.items()}
    return encrypt(text, reverse_key)

# Create a random cipher key
cipher_key = create_cipher_key()

# Show the mapping
print("CIPHER KEY MAPPING:")
print("="*40)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f"Plain:  {alphabet}")
print(f"Cipher: {''.join(cipher_key[c] for c in alphabet)}")

# Encrypt a message
message = input("Enter the message to encrypt: ")
encrypted = encrypt(message, cipher_key)
decrypted = decrypt(encrypted, cipher_key)

print("\n" + "="*40)
print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")