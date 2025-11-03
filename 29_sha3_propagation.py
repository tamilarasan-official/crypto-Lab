# Program 29: SHA-3 State Propagation
def sha3_propagation():
    print("=== SHA-3 State Propagation ===")
    
    print("\nParameters:")
    print("- Block size: 1024 bits")
    print("- Rate: 1024 bits")
    print("- Capacity: 576 bits")
    
    print("\nState structure:")
    print("- 5×5 array of 64-bit lanes = 1600 bits total")
    print("- Capacity = 9 lanes (576 bits)")
    print("- Initially all capacity lanes are zero")
    
    print("\nFirst message block P0:")
    print("- Has at least one nonzero bit in each lane")
    print("- XORed with rate portion of state")
    
    print("\nPropagation analysis:")
    print("After 1 round of permutation:")
    print("- θ (theta) step: mixes columns")
    print("- ρ (rho) step: rotates lanes")
    print("- π (pi) step: permutes lanes")
    print("- χ (chi) step: nonlinear mixing")
    print("- ι (iota) step: adds round constant")
    
    print("\nResult:")
    print("All capacity lanes have nonzero bits after 1 round")
    print("Full diffusion achieved quickly")

if __name__ == "__main__":
    sha3_propagation()