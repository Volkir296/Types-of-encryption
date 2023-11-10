def encrypt(pk, plaintext):
    t = tuple(int(item) for item in pk.split(' '))
    key, n = t
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)