# Program 36: Affine Cipher (Duplicate)
# Same as Program 5
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        return "Error: 'a' must be coprime with 26"
    result = ""
    for char in plaintext.upper():
        if char.isalpha():
            result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            result += char
    return result

def main():
    print("=== Affine Caesar Cipher ===")
    print("Valid 'a' values: 1,3,5,7,9,11,15,17,19,21,23,25")
    text = input("Enter plaintext: ")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(f"Encrypted: {affine_encrypt(text, a, b)}")

if __name__ == "__main__":
    main()