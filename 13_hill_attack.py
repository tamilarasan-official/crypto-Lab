# Program 13: Hill Cipher Known Plaintext Attack
import numpy as np

def hill_attack():
    print("=== Hill Cipher Known Plaintext Attack ===")
    print("Given plaintext-ciphertext pairs, find key matrix K")
    print("\nC = K × P (mod 26)")
    print("K = C × P^(-1) (mod 26)")
    
    plaintext = input("Enter plaintext pairs (e.g., 'HELP'): ").upper()
    ciphertext = input("Enter ciphertext pairs: ").upper()
    
    P = np.array([[ord(plaintext[0])-65, ord(plaintext[2])-65],
                   [ord(plaintext[1])-65, ord(plaintext[3])-65]])
    
    C = np.array([[ord(ciphertext[0])-65, ord(ciphertext[2])-65],
                   [ord(ciphertext[1])-65, ord(ciphertext[3])-65]])
    
    det_P = int(np.linalg.det(P)) % 26
    det_inv = pow(det_P, -1, 26)
    P_inv = (det_inv * np.round(det_P * np.linalg.inv(P)).astype(int)) % 26
    
    K = np.dot(C, P_inv) % 26
    
    print(f"\nRecovered key matrix:")
    print(K.astype(int))

if __name__ == "__main__":
    hill_attack()