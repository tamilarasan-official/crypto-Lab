def caesar_cipher(user_text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    
    for char in user_text:
        if char.isalpha():  # Check if it's a letter
            # Get starting point: 'A' for uppercase, 'a' for lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using % 26
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-letters as is
    
    return result


# Test the cipher with all shifts from 1 to 25
user_text = input("Enter text to encrypt: ")

print(f"Original: {user_text}\n")

for k in range(1, 26):
    encrypted = caesar_cipher(user_text, k)
    print(f"Shift {k}: {encrypted}")

# Show specific encryption example
print("\n" + "="*40)
print("EXAMPLE: Encrypt with shift of 3")
print("="*40)
my_text = user_text
my_shift = 3
encrypted_text = caesar_cipher(my_text, my_shift)
print(f"Original text:   {my_text}")
print(f"Shift value:     {my_shift}")
print(f"Encrypted text:  {encrypted_text}")