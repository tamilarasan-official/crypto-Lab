# Program 32: DSA vs RSA Signatures
def dsa_vs_rsa_signatures():
    print("=== DSA vs RSA Signature Comparison ===")
    
    print("\nDSA (Digital Signature Algorithm):")
    print("- Uses random k for each signature")
    print("- Same message → Different signatures each time")
    print("- Signature includes randomness")
    print("- Format: (r, s) where r depends on k")
    
    print("\nRSA Signatures:")
    print("- Deterministic process")
    print("- Same message → Same signature always")
    print("- Signature: S = M^d mod n")
    
    print("\nImplications:")
    print("\n1. Randomness:")
    print("   DSA: Provides randomness, harder to analyze")
    print("   RSA: Reproducible, easier to verify/cache")
    
    print("\n2. Security:")
    print("   DSA: k must be secret and random (critical!)")
    print("   RSA: No randomness requirement")
    
    print("\n3. Verification:")
    print("   DSA: Cannot predict signature")
    print("   RSA: Can precompute signature")
    
    print("\n4. Non-repudiation:")
    print("   Both provide non-repudiation")
    print("   DSA randomness doesn't affect this")

if __name__ == "__main__":
    dsa_vs_rsa_signatures()