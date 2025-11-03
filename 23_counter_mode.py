# Program 23: Counter Mode Encryption
def counter_mode():
    print("=== Counter Mode Encryption ===")
    
    plaintext_blocks = ["00000001", "00000010", "00000100"]
    key = "0111111101"
    counter_start = 0
    
    print(f"Plaintext blocks: {plaintext_blocks}")
    print(f"Key: {key}")
    print(f"Counter starts at: {counter_start:08b}")
    
    print("\nCounter Mode process:")
    print("C1 = P1 ⊕ E(K, Counter+0)")
    print("C2 = P2 ⊕ E(K, Counter+1)")
    print("C3 = P3 ⊕ E(K, Counter+2)")
    
    print("\nExpected ciphertext: 00111000 01001111 00110010")
    
    print("\nAdvantages:")
    print("- Parallel encryption/decryption")
    print("- Random access to blocks")
    print("- No error propagation")

if __name__ == "__main__":
    counter_mode()