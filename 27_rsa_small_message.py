# Program 27: RSA Small Message Attack
def rsa_small_message_attack():
    print("=== RSA Small Message Attack ===")
    
    print("\nScenario:")
    print("- Encrypting single characters (A-Z = 0-25)")
    print("- Each character encrypted separately")
    print("- Using RSA with large e and n")
    
    print("\nWhy this is INSECURE:")
    print("1. Only 26 possible plaintexts")
    print("2. Attacker can:")
    print("   - Encrypt all 26 letters")
    print("   - Build lookup table")
    print("   - Match ciphertext to plaintext")
    
    print("\nDemonstration:")
    e, n = 31, 3599
    print(f"\nPublic key: e={e}, n={n}")
    print("\nEncrypting A-Z:")
    
    for i in range(26):
        char = chr(65 + i)
        ciphertext = pow(i, e, n)
        print(f"{char} ({i:2d}) → {ciphertext:4d}")
    
    print("\nSolution: Use padding (OAEP)")
    print("- Adds randomness")
    print("- Makes plaintext large")
    print("- Prevents dictionary attacks")

if __name__ == "__main__":
    rsa_small_message_attack()