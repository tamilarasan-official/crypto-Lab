# Program 26: RSA Key Reuse Security
def rsa_key_reuse():
    print("=== RSA Key Reuse Analysis ===")
    
    print("\nScenario:")
    print("- Bob's private key d is leaked")
    print("- Bob wants to generate new key pair")
    print("- Question: Can he reuse modulus n?")
    
    print("\nAnswer: NO - This is UNSAFE!")
    
    print("\nReasons:")
    print("1. If attacker has old private key d:")
    print("   - They know φ(n) from e and d")
    print("   - They can factor n using φ(n)")
    print("   - Any new key pair with same n is compromised")
    
    print("\n2. Even without old key:")
    print("   - Reusing n is bad practice")
    print("   - Multiple keys with same modulus can be attacked")
    
    print("\nCorrect approach:")
    print("- Generate completely new n (new p and q)")
    print("- Generate new e and d")
    print("- Discard all old key material")

if __name__ == "__main__":
    rsa_key_reuse()