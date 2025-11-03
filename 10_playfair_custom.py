# Program 10: Playfair with Custom Matrix
def playfair_encrypt_custom():
    matrix = [
        ['M','F','H','I','K'],
        ['U','N','O','P','Q'],
        ['Z','V','W','X','Y'],
        ['E','L','A','R','G'],
        ['D','S','T','B','C']
    ]
    
    def find_pos(char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
    
    plaintext = "MUSTSSEEYOUOVERCADOGANWESTCOMINGATONCE"
    result = ""
    
    for i in range(0, len(plaintext), 2):
        r1, c1 = find_pos(plaintext[i])
        r2, c2 = find_pos(plaintext[i+1])
        
        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {result}")

if __name__ == "__main__":
    playfair_encrypt_custom()