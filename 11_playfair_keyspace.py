# Program 11: Playfair Key Space Calculation
import math

def playfair_keyspace():
    print("=== Playfair Cipher Key Space ===")
    
    # Total possible arrangements of 25 letters
    total_keys = math.factorial(25)
    power_of_2 = math.log2(total_keys)
    
    print(f"Total possible keys: 25! = {total_keys}")
    print(f"Approximately: 2^{int(power_of_2)}")
    
    # Accounting for duplicates (different keywords producing same matrix)
    # Effectively unique keys ≈ 25!/25 due to rotational equivalence
    effective_keys = total_keys / 25
    effective_power = math.log2(effective_keys)
    
    print(f"\nEffectively unique keys: {effective_keys:.2e}")
    print(f"Approximately: 2^{int(effective_power)}")

if __name__ == "__main__":
    playfair_keyspace()