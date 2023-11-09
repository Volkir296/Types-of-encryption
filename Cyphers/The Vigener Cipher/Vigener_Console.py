from VigenerFun import vigenere_cipher

plaintext = 'ATTACKATDAWN'
keyword = 'LEMON'

ciphertext = vigenere_cipher(plaintext, keyword, mode='encrypt')
print(ciphertext)  # Output: LXFOPVEFRNHR

decrypted_text = vigenere_cipher(ciphertext, keyword, mode='decrypt')
print(decrypted_text)  # Output: ATTACKATDAWN