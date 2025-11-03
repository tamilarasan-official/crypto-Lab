# Program 38: Hill Cipher Attack (Duplicate)
# Same as Program 13
import numpy as np

def hill_attack():
    print("=== Hill Cipher Known Plaintext Attack ===")
    print("Given sufficient plaintext-ciphertext pairs:")
    print("\nC = K × P (mod 26)")
    print("Solve for K: K = C × P^(-1) (mod 26)")
    
    print("\nFor 2×2 matrix, need 2 character pairs")
    print("For 3×3 matrix, need 3 character pairs")
    
    print("\nChosen plaintext attack is even easier:")
    print("Choose P = I (identity matrix)")
    print("Then C = K directly!")

if __name__ == "__main__":
    hill_attack()