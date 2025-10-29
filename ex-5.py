# Affine Caesar Cipher - Simplified Version
# Formula: C = (ap + b) mod 26

import math

def gcd(a, b):
    """Calculate Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Find modular multiplicative inverse of a mod m."""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(plaintext, a, b):
    """Encrypt using formula: C = (ap + b) mod 26"""
    result = ""
    for char in plaintext:
        if char.isalpha():
            p = ord(char.upper()) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += char
    return result

def decrypt(ciphertext, a, b):
    """Decrypt using formula: P = a_inv(C - b) mod 26"""
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('A'))
        else:
            result += char
    return result

# Main Program
print("AFFINE CAESAR CIPHER")
print("Formula: C = (ap + b) mod 26\n")

# Answer the questions
print("(a) Limitations on b: NONE (any value 0-25 is valid)")
print("(b) Invalid values of a: Any 'a' where gcd(a,26) ≠ 1\n")

# Show valid and invalid values
valid_a = [i for i in range(1, 26) if gcd(i, 26) == 1]
invalid_a = [i for i in range(1, 26) if gcd(i, 26) != 1]

print(f"Valid a values:   {valid_a}")
print(f"Invalid a values: {invalid_a}\n")

# Example: Why a=2 fails
print("Example: Why a=2 is invalid:")
a, b = 2, 3
print(f"E([2,3], 0)  = (2×0 + 3) mod 26 = {(a*0 + b) % 26}")
print(f"E([2,3], 13) = (2×13 + 3) mod 26 = {(a*13 + b) % 26}")
print("Both give 3 - NOT one-to-one!\n")

# Get user input
a = int(input(f"Enter a (choose from {valid_a}): "))
b = int(input("Enter b (0-25): "))

# Validate
if gcd(a, 26) != 1:
    print(f"Error: a={a} is invalid! Must be coprime with 26.")
else:
    message = input("Enter message: ")
    
    encrypted = encrypt(message, a, b)
    decrypted = decrypt(encrypted, a, b)
    
    print(f"\nPlaintext:  {message}")
    print(f"Ciphertext: {encrypted}")
    print(f"Decrypted:  {decrypted}")