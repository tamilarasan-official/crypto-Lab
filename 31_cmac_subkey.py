# Program 31: CMAC Subkey Generation
def cmac_subkey_generation():
    print("=== CMAC Subkey Generation ===")
    
    print("\nAlgorithm:")
    print("1. L = E(K, 0^n) - Encrypt block of zeros")
    print("2. If MSB(L) = 0: K1 = L << 1")
    print("   If MSB(L) = 1: K1 = (L << 1) ⊕ Rb")
    print("3. If MSB(K1) = 0: K2 = K1 << 1")
    print("   If MSB(K1) = 1: K2 = (K1 << 1) ⊕ Rb")
    
    print("\nConstants (Rb):")
    print("- 64-bit blocks: Rb = 0x1B")
    print("  Binary: 00011011")
    print("- 128-bit blocks: Rb = 0x87")
    print("  Binary: 10000111")
    
    print("\nWhy left shift and XOR?")
    print("- Implements multiplication by x in GF(2^n)")
    print("- Ensures subkeys are independent")
    print("- XOR with Rb handles overflow")
    
    print("\nExample (128-bit):")
    L = "0x2B7E151628AED2A6ABF7158809CF4F3C"
    print(f"L = {L}")
    print("K1 = L << 1 = (left shift)")
    print("K2 = K1 << 1 = (left shift)")

if __name__ == "__main__":
    cmac_subkey_generation()