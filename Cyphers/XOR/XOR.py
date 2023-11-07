def xor_encrypt_decrypt(message, key):
    encrypted = ""
    for i in range(len(message)):
        # Применяем операцию XOR между символом сообщения и соответствующим символом ключа
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted

# Пример использования
message = "Hello, world!"
key = "secret"

encrypted_message = xor_encrypt_decrypt(message, key)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Расшифрованное сообщение:", decrypted_message)