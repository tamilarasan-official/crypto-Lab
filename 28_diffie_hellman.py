# Program 28: Diffie-Hellman Key Exchange
def diffie_hellman():
    print("=== Diffie-Hellman Key Exchange ===")
    
    # Public parameters
    p = int(input("Enter prime p (e.g., 23): ") or "23")
    g = int(input("Enter generator g (e.g., 5): ") or "5")
    
    print(f"\nPublic parameters: p={p}, g={g}")
    
    # Alice's private key
    a = int(input("\nAlice's private key a: ") or "6")
    A = pow(g, a, p)
    print(f"Alice sends: A = g^a mod p = {A}")
    
    # Bob's private key
    b = int(input("\nBob's private key b: ") or "15")
    B = pow(g, b, p)
    print(f"Bob sends: B = g^b mod p = {B}")
    
    # Shared secret
    shared_alice = pow(B, a, p)
    shared_bob = pow(A, b, p)
    
    print(f"\nAlice computes: B^a mod p = {shared_alice}")
    print(f"Bob computes: A^b mod p = {shared_bob}")
    print(f"\nShared secret: {shared_alice}")
    
    if shared_alice == shared_bob:
        print("✓ Key exchange successful!")

if __name__ == "__main__":
    diffie_hellman()