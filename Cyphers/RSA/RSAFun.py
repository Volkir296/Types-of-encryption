def encrypt(pk, plaintext):
    t = tuple(int(item) for item in pk.split(' '))
    key, n = t
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    t = tuple(int(item) for item in pk.split(' '))
    key, n = t

    k = list(int(item) for item in ciphertext.split(' '))

    plain = [chr(pow(char, key, n)) for char in k]
    return ''.join(plain)