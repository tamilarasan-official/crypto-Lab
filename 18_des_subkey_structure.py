# Program 18: DES Subkey Structure
def des_subkey_structure():
    print("=== DES Subkey Structure ===")
    print("\nInitial 56-bit key split into:")
    print("- C0: Left 28 bits")
    print("- D0: Right 28 bits")
    print("\nEach subkey (48 bits):")
    print("- First 24 bits: Selected from C register (28 bits)")
    print("- Second 24 bits: Selected from D register (28 bits)")
    print("\nPC-2 permutation selects 48 bits from 56-bit concatenation")
    print("The two halves come from disjoint subsets")

if __name__ == "__main__":
    des_subkey_structure()