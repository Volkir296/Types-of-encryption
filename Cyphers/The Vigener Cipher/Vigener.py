def vigenere_cipher(text, key, mode='encrypt'):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    key = key.upper()
    result = ''
    key_index = 0

    for char in text:
        if char in alphabet:
            if mode == 'encrypt':
                char_index = (alphabet.index(char) + alphabet.index(key[key_index])) % 26
            elif mode == 'decrypt':
                char_index = (alphabet.index(char) - alphabet.index(key[key_index])) % 26
            result += alphabet[char_index]
            key_index = (key_index + 1) % len(key)
        else:
            result += char

    return result

plaintext = 'ATTACKATDAWN'
keyword = 'LEMON'

ciphertext = vigenere_cipher(plaintext, keyword, mode='encrypt')
print(ciphertext)  # Output: LXFOPVEFRNHR

decrypted_text = vigenere_cipher(ciphertext, keyword, mode='decrypt')
print(decrypted_text)  # Output: ATTACKATDAWN
