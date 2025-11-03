# Program 34: Padding in Block Ciphers
def padding_explanation():
    print("=== Block Cipher Padding ===")
    
    print("\nRequirement:")
    print("Plaintext must be multiple of block size")
    print("- DES/3DES: 64-bit blocks (8 bytes)")
    print("- AES: 128-bit blocks (16 bytes)")
    
    print("\nPadding method:")
    print("Add '1' bit followed by '0' bits")
    
    print("\nExamples (8-byte blocks):")
    print("\n1. Message: 7 bytes")
    print("   Padding: 10000000 (1 byte)")
    
    print("\n2. Message: 5 bytes")
    print("   Padding: 10000000 00000000 00000000 (3 bytes)")
    
    print("\n3. Message: 8 bytes (complete block)")
    print("   Padding: 10000000 00000000 ... (8 bytes)")
    print("   Add entire padding block!")
    
    print("\nWhy always pad?")
    print("- Receiver knows to remove padding")
    print("- No ambiguity about message end")
    print("- Security: prevents certain attacks")
    print("- Consistency: same process for all messages")
    
    print("\nRemoving padding:")
    print("- Find last '1' bit")
    print("- Remove it and all following '0' bits")

if __name__ == "__main__":
    padding_explanation()