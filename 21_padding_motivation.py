# Program 21: Padding Motivation in Block Ciphers
def padding_motivation():
    print("=== Motivation for Padding ===")
    
    print("\nWhy always pad, even when block is complete?")
    print("\n1. Unambiguous Message Delimitation:")
    print("   - Receiver can always identify padding")
    print("   - No confusion about message end")
    
    print("\n2. Security:")
    print("   - Prevents padding oracle attacks")
    print("   - Consistent handling of all messages")
    
    print("\n3. Integrity:")
    print("   - Can detect truncation attacks")
    print("   - Ensures complete message received")
    
    print("\n4. Implementation:")
    print("   - Simpler code (always remove padding)")
    print("   - No special cases to handle")
    
    print("\nPadding scheme: 1 bit followed by zero bits")
    print("Example: ...0001 or ...0100 or ...1000 or ...10000000")

if __name__ == "__main__":
    padding_motivation()