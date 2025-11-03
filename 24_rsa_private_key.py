# Program 24: RSA Private Key Calculation
def rsa_private_key():
    print("=== RSA Private Key Calculation ===")
    e = 31
    n = 3599
    
    print(f"Public key: e = {e}, n = {n}")
    
    # Factor n using trial division
    print("\nFactoring n...")
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            q = n // p
            print(f"Found: p = {p}, q = {q}")
            
            # Calculate phi(n)
            phi_n = (p - 1) * (q - 1)
            print(f"φ(n) = (p-1)(q-1) = {phi_n}")
            
            # Calculate d using extended Euclidean algorithm
            d = pow(e, -1, phi_n)
            print(f"\nPrivate key: d = {d}")
            
            # Verify
            print(f"\nVerification: (e × d) mod φ(n) = {(e * d) % phi_n}")
            return d
    
    print("Could not factor n")
    return None

if __name__ == "__main__":
    rsa_private_key()