# Program 19: CBC Mode with 3DES
def cbc_3des_comparison():
    print("=== CBC Mode with 3DES ===")
    print("\nOptions:")
    print("a) Security: 3DES with three independent keys (EDE3)")
    print("   - Most secure: K1, K2, K3 all different")
    print("   - Effective key length: 168 bits")
    
    print("\nb) Performance: 3DES with two keys (EDE2)")
    print("   - Faster: K1 = K3, only K2 is different")
    print("   - Effective key length: 112 bits")
    print("   - Better performance, acceptable security")
    
    choice = input("\nChoose (a/b): ").lower()
    if choice == 'a':
        print("\nRecommendation: Use EDE3 mode for maximum security")
    else:
        print("\nRecommendation: Use EDE2 mode for better performance")

if __name__ == "__main__":
    cbc_3des_comparison()