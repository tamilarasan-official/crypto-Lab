# Program 12: Hill Cipher (2x2)
import numpy as np

def hill_encrypt():
    plaintext = "meetmeattheusualplaceattenratherthaneightoclock"
    plaintext = plaintext.upper().replace(" ", "")
    
    key = np.array([[9, 4], [5, 7]])
    
    # Convert to numbers
    nums = [ord(c) - 65 for c in plaintext]
    if len(nums) % 2:
        nums.append(23)  # Pad with X
    
    # Encrypt
    ciphertext_nums = []
    for i in range(0, len(nums), 2):
        vector = np.array([nums[i], nums[i+1]])
        encrypted = np.dot(key, vector) % 26
        ciphertext_nums.extend(encrypted)
    
    ciphertext = ''.join(chr(n + 65) for n in ciphertext_nums)
    
    print("Key matrix:")
    print(key)
    print(f"\nPlaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    
    # Decrypt
    det = int(np.linalg.det(key)) % 26
    det_inv = pow(det, -1, 26)
    key_inv = (det_inv * np.round(det * np.linalg.inv(key)).astype(int)) % 26
    
    decrypted_nums = []
    for i in range(0, len(ciphertext_nums), 2):
        vector = np.array([ciphertext_nums[i], ciphertext_nums[i+1]])
        decrypted = np.dot(key_inv, vector) % 26
        decrypted_nums.extend(decrypted.astype(int))
    
    decrypted = ''.join(chr(n + 65) for n in decrypted_nums)
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    hill_encrypt()