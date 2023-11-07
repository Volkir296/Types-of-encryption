def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(encrypted_text)  # Output: "Khoor, Zruog!"