# Program 17: DES Key Schedule for Decryption
def des_key_schedule():
    print("=== DES Key Generation for Decryption ===")
    print("\nFor encryption:")
    print("Keys used: K1, K2, K3, ..., K15, K16")
    print("\nFor decryption:")
    print("Keys used: K16, K15, K14, ..., K2, K1 (reverse order)")
    print("\nShift schedule remains same, applied in reverse")
    print("This maintains the Feistel structure property")

if __name__ == "__main__":
    des_key_schedule()