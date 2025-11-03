# Program 3: Playfair Cipher
def create_matrix(key):
    key = key.upper().replace('J', 'I')
    key = ''.join(dict.fromkeys(key))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_str = key + ''.join(c for c in alphabet if c not in key)
    return [list(matrix_str[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    matrix = create_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    
    digraphs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else 'X'
        digraphs.append(a + 'X' if a == b else a + b)
        i += 1 if a == b else 2
    
    result = ""
    for dg in digraphs:
        r1, c1 = find_position(matrix, dg[0])
        r2, c2 = find_position(matrix, dg[1])
        
        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    
    return result

def main():
    print("=== Playfair Cipher ===")
    keyword = input("Enter keyword: ")
    plaintext = input("Enter plaintext: ")
    print(f"Encrypted: {playfair_encrypt(plaintext, keyword)}")

if __name__ == "__main__":
    main()