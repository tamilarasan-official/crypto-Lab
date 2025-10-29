# Playfair Cipher Implementation

def create_playfair_matrix(key):
    """
    Creates a 5x5 matrix using the given keyword.
    Combines I and J into single cell.
    """
    # Remove duplicates from key and convert to uppercase
    key = key.upper().replace("J", "I")
    matrix_letters = []
    
    # Add unique letters from key
    for letter in key:
        if letter.isalpha() and letter not in matrix_letters:
            matrix_letters.append(letter)
    
    # Add remaining letters of alphabet (excluding J)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # No J
    for letter in alphabet:
        if letter not in matrix_letters:
            matrix_letters.append(letter)
    
    # Create 5x5 matrix
    matrix = []
    for i in range(5):
        row = matrix_letters[i*5:(i+1)*5]
        matrix.append(row)
    
    return matrix


def display_matrix(matrix):
    """Display the 5x5 Playfair matrix."""
    print("\nPlayfair Matrix:")
    print("-" * 21)
    for row in matrix:
        print("| " + " ".join(row) + " |")
    print("-" * 21)


def find_position(matrix, letter):
    """Find the row and column position of a letter in the matrix."""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
    return None


def prepare_plaintext(text):
    """
    Prepare plaintext for encryption:
    - Convert to uppercase
    - Replace J with I
    - Split into digraphs (pairs)
    - Add X between duplicate letters
    - Add X at end if odd length
    """
    text = text.upper().replace("J", "I")
    # Remove non-alphabetic characters
    text = ''.join(filter(str.isalpha, text))
    
    # Split into digraphs
    digraphs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            # Last letter, add X
            digraphs.append(text[i] + 'X')
            i += 1
        elif text[i] == text[i+1]:
            # Same letters, add X between them
            digraphs.append(text[i] + 'X')
            i += 1
        else:
            # Normal pair
            digraphs.append(text[i] + text[i+1])
            i += 2
    
    return digraphs


def encrypt_digraph(matrix, digraph):
    """
    Encrypt a pair of letters using Playfair rules:
    1. Same row: shift right
    2. Same column: shift down
    3. Rectangle: swap columns
    """
    letter1, letter2 = digraph[0], digraph[1]
    row1, col1 = find_position(matrix, letter1)
    row2, col2 = find_position(matrix, letter2)
    
    if row1 == row2:
        # Same row: shift right (wrap around)
        encrypted1 = matrix[row1][(col1 + 1) % 5]
        encrypted2 = matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column: shift down (wrap around)
        encrypted1 = matrix[(row1 + 1) % 5][col1]
        encrypted2 = matrix[(row2 + 1) % 5][col2]
    else:
        # Rectangle: swap columns
        encrypted1 = matrix[row1][col2]
        encrypted2 = matrix[row2][col1]
    
    return encrypted1 + encrypted2


def decrypt_digraph(matrix, digraph):
    """
    Decrypt a pair of letters using Playfair rules (reverse):
    1. Same row: shift left
    2. Same column: shift up
    3. Rectangle: swap columns
    """
    letter1, letter2 = digraph[0], digraph[1]
    row1, col1 = find_position(matrix, letter1)
    row2, col2 = find_position(matrix, letter2)
    
    if row1 == row2:
        # Same row: shift left (wrap around)
        decrypted1 = matrix[row1][(col1 - 1) % 5]
        decrypted2 = matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # Same column: shift up (wrap around)
        decrypted1 = matrix[(row1 - 1) % 5][col1]
        decrypted2 = matrix[(row2 - 1) % 5][col2]
    else:
        # Rectangle: swap columns
        decrypted1 = matrix[row1][col2]
        decrypted2 = matrix[row2][col1]
    
    return decrypted1 + decrypted2


def encrypt_playfair(plaintext, key):
    """Encrypt plaintext using Playfair cipher."""
    matrix = create_playfair_matrix(key)
    digraphs = prepare_plaintext(plaintext)
    
    ciphertext = ""
    for digraph in digraphs:
        ciphertext += encrypt_digraph(matrix, digraph)
    
    return ciphertext, matrix, digraphs


def decrypt_playfair(ciphertext, key):
    """Decrypt ciphertext using Playfair cipher."""
    matrix = create_playfair_matrix(key)
    
    # Split ciphertext into digraphs
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    plaintext = ""
    for digraph in digraphs:
        plaintext += decrypt_digraph(matrix, digraph)
    
    return plaintext, matrix


# Main Program
print("=" * 60)
print("PLAYFAIR CIPHER")
print("=" * 60)
print()

# Get keyword from user
keyword = input("Enter the keyword: ")

# Get plaintext from user
plaintext = input("Enter the plaintext message: ")
print()

# Encrypt the message
ciphertext, matrix, digraphs = encrypt_playfair(plaintext, keyword)

# Display the matrix
display_matrix(matrix)
print()

# Show the digraphs
print(f"Plaintext digraphs: {' '.join(digraphs)}")
print()

# Display results
print(f"Original Plaintext:  {plaintext}")
print(f"Encrypted Ciphertext: {ciphertext}")
print()

# Decrypt to verify
decrypted, _ = decrypt_playfair(ciphertext, keyword)
print(f"Decrypted Plaintext:  {decrypted}")
print()

# Additional example
print("=" * 60)
print("EXAMPLE WITH KEYWORD 'MONARCHY'")
print("=" * 60)

#keyword = "MONARCHY"
#plaintext = "HELLO WORLD"

example_cipher, example_matrix, example_digraphs = encrypt_playfair(plaintext, keyword)
display_matrix(example_matrix)
print()
print(f"Plaintext:  {plaintext}")
print(f"Digraphs:   {' '.join(example_digraphs)}")
print(f"Ciphertext: {example_cipher}")
print()

example_decrypt, _ = decrypt_playfair(example_cipher, keyword)
print(f"Decrypted:  {example_decrypt}")
print()

print("=" * 60)
print("RESULT:")
print("=" * 60)
print("The Playfair cipher successfully encrypts plaintext by")
print("processing pairs of letters using a 5x5 keyword matrix.")
print("Rules applied:")
print("1. Same row → shift right")
print("2. Same column → shift down")
print("3. Rectangle → swap columns")
print("=" * 60)