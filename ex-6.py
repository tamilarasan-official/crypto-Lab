# Affine Cipher Breaker using Frequency Analysis

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

def frequency_analysis(ciphertext):
    """Count frequency of each letter in ciphertext."""
    freq = {}
    for char in ciphertext.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    # Sort by frequency (descending)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

def solve_affine_key(c1, c2, p1, p2):
    """
    Solve for 'a' and 'b' in affine cipher given:
    c1 = (a * p1 + b) mod 26
    c2 = (a * p2 + b) mod 26
    
    Solving: a = (c1 - c2) * (p1 - p2)^-1 mod 26
             b = (c1 - a * p1) mod 26
    """
    # Convert letters to numbers (A=0, B=1, ..., Z=25)
    c1_num = ord(c1) - ord('A')
    c2_num = ord(c2) - ord('A')
    p1_num = ord(p1) - ord('A')
    p2_num = ord(p2) - ord('A')
    
    # Calculate (p1 - p2) mod 26
    p_diff = (p1_num - p2_num) % 26
    
    # Find modular inverse of (p1 - p2)
    p_diff_inv = mod_inverse(p_diff, 26)
    
    if p_diff_inv is None:
        return None, None
    
    # Calculate a = (c1 - c2) * (p1 - p2)^-1 mod 26
    c_diff = (c1_num - c2_num) % 26
    a = (c_diff * p_diff_inv) % 26
    
    # Check if 'a' is valid (must be coprime with 26)
    if gcd(a, 26) != 1:
        return None, None
    
    # Calculate b = (c1 - a * p1) mod 26
    b = (c1_num - a * p1_num) % 26
    
    return a, b

def decrypt_affine(ciphertext, a, b):
    """Decrypt ciphertext using affine cipher with key (a, b)."""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            c = ord(char.upper()) - ord('A')
            p = (a_inv * (c - b)) % 26
            decrypted_char = chr(p + ord('A'))
            plaintext += decrypted_char if is_upper else decrypted_char.lower()
        else:
            plaintext += char
    
    return plaintext

# Main Program
print("=" * 70)
print("AFFINE CIPHER BREAKER - FREQUENCY ANALYSIS")
print("=" * 70)
print()

# Given information from the problem
print("Given Information:")
print("- Most frequent ciphertext letter: B")
print("- Second most frequent ciphertext letter: U")
print()

# English letter frequencies (most common letters)
print("English Language Facts:")
print("- Most frequent letter in English: E")
print("- Second most frequent letter in English: T")
print()

# Problem setup
cipher_most_freq = 'B'      # Most frequent in ciphertext
cipher_second_freq = 'U'    # Second most frequent in ciphertext
plain_most_freq = 'E'       # Most frequent in English
plain_second_freq = 'T'     # Second most frequent in English

print("Assumption: Ciphertext frequencies match English plaintext frequencies")
print(f"- Cipher 'B' → Plain 'E'")
print(f"- Cipher 'U' → Plain 'T'")
print()

# Solve for the key
print("=" * 70)
print("SOLVING FOR KEY (a, b)")
print("=" * 70)
print()

print("Using equations:")
print(f"  B = (a × E + b) mod 26  →  1 = (a × 4 + b) mod 26")
print(f"  U = (a × T + b) mod 26  →  20 = (a × 19 + b) mod 26")
print()

a, b = solve_affine_key(cipher_most_freq, cipher_second_freq, 
                        plain_most_freq, plain_second_freq)

if a is None:
    print("Could not find valid key with these assumptions!")
else:
    print(f"Solution found:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  Modular inverse of a: {mod_inverse(a, 26)}")
    print()
    
    # Verify the solution
    print("Verification:")
    e_val = ord('E') - ord('A')
    t_val = ord('T') - ord('A')
    b_check = (a * e_val + b) % 26
    u_check = (a * t_val + b) % 26
    
    print(f"  E (4) → ({a} × 4 + {b}) mod 26 = {b_check} → {chr(b_check + ord('A'))}")
    print(f"  T (19) → ({a} × 19 + {b}) mod 26 = {u_check} → {chr(u_check + ord('A'))}")
    print()

# Example: Test with actual ciphertext
print("=" * 70)
print("TESTING WITH EXAMPLE CIPHERTEXT")
print("=" * 70)
print()

# Get ciphertext from user
ciphertext = input("Enter the ciphertext to decrypt (or press Enter for example): ")

if not ciphertext.strip():
    # Use example ciphertext encrypted with the found key
    ciphertext = "BUBU TSUBU IURKBU"
    print(f"Using example: {ciphertext}")

print()

# Perform frequency analysis on the given ciphertext
print("Frequency Analysis of Ciphertext:")
freq = frequency_analysis(ciphertext)
for i, (letter, count) in enumerate(freq[:5]):
    print(f"  {i+1}. {letter}: {count} times")
print()

# Decrypt using the found key
if a is not None and b is not None:
    decrypted = decrypt_affine(ciphertext, a, b)
    
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Key found: a = {a}, b = {b}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Plaintext:  {decrypted}")
    print("=" * 70)
    print()

# Try alternative assumptions if needed
print("=" * 70)
print("ALTERNATIVE APPROACHES")
print("=" * 70)
print()
print("If the decryption doesn't make sense, try:")
print("1. Different plaintext letter assumptions (e.g., A, O, I, N, S)")
print("2. Swap the frequency order (B→T, U→E)")
print("3. Check if punctuation/spaces affect frequency counts")
print()

# Try alternative: swap E and T
print("Alternative Key (assuming B→T, U→E):")
a_alt, b_alt = solve_affine_key(cipher_most_freq, cipher_second_freq, 
                                plain_second_freq, plain_most_freq)
if a_alt is not None:
    print(f"  a = {a_alt}, b = {b_alt}")
    if ciphertext.strip():
        decrypted_alt = decrypt_affine(ciphertext, a_alt, b_alt)
        print(f"  Decrypted: {decrypted_alt}")
else:
    print("  No valid key found for this assumption")
print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print("Frequency analysis breaks affine ciphers by:")
print("1. Finding most frequent letters in ciphertext")
print("2. Assuming they correspond to common English letters (E, T)")
print("3. Solving the system of equations to find a and b")
print("4. Decrypting the entire message with the found key")
print("=" * 70)