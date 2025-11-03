# Program 6: Break Affine Cipher
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def break_affine():
    print("=== Break Affine Cipher ===")
    most_freq = input("Most frequent ciphertext letter: ").upper()
    second_freq = input("Second most frequent letter: ").upper()
    
    c1 = ord(most_freq) - 65
    c2 = ord(second_freq) - 65
    
    # Assuming most frequent plaintext letters are E(4) and T(19)
    p1, p2 = 4, 19
    
    valid_a = [1,3,5,7,9,11,15,17,19,21,23,25]
    
    for a in valid_a:
        b = (c1 - a * p1) % 26
        if (a * p2 + b) % 26 == c2:
            print(f"\nFound key: a={a}, b={b}")
            return a, b
    
    print("Could not break cipher with E and T assumption")
    return None, None

if __name__ == "__main__":
    break_affine()