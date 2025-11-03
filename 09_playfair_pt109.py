# Program 9: Decrypt PT-109 Message
def playfair_decrypt(ciphertext, matrix):
    def find_pos(char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
    
    result = ""
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_pos(ciphertext[i])
        r2, c2 = find_pos(ciphertext[i+1])
        
        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    
    return result

def main():
    print("=== Decrypt PT-109 Message ===")
    cipher = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYDSEDQ"
    cipher = cipher.replace(" ", "")
    
    # Use appropriate Playfair matrix
    key = input("Enter keyword for matrix: ").upper()
    # Create matrix and decrypt
    print(f"Ciphertext: {cipher}")
    print("Decrypt using playfair matrix")

if __name__ == "__main__":
    main()