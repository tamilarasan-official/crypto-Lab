# Program 25: RSA Common Factor Attack
import math

def rsa_common_factor_attack():
    print("=== RSA Common Factor Attack ===")
    
    print("\nScenario:")
    print("- We have ciphertext blocks encrypted with RSA")
    print("- n = p × q (public modulus)")
    print("- Someone tells us a plaintext block shares a factor with n")
    
    print("\nAttack:")
    print("If plaintext P shares a factor with n:")
    print("1. Compute gcd(P, n)")
    print("2. This gives us either p or q")
    print("3. We can then find the other factor")
    print("4. Calculate φ(n) = (p-1)(q-1)")
    print("5. Find private key d")
    
    print("\nExample:")
    n = 3599
    plaintext = 59  # This shares factor with n
    
    factor = math.gcd(plaintext, n)
    print(f"n = {n}")
    print(f"Plaintext = {plaintext}")
    print(f"gcd(plaintext, n) = {factor}")
    
    if factor > 1 and factor < n:
        other_factor = n // factor
        print(f"\nFactors found: {factor} and {other_factor}")
        print("RSA system is broken!")

if __name__ == "__main__":
    rsa_common_factor_attack()