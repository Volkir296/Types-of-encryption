from XORFun import xor_encrypt_decrypt

# Пример использования
message = "Hello, world!"
key = "secret"

encrypted_message = xor_encrypt_decrypt(message, key)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Расшифрованное сообщение:", decrypted_message)


# Пример использования с помощью данных, вводимых пользователем
message = input("Введите фразу, которую хотите зашифровать:\n")
key = input("Введите фразу-ключ, которой фраза будет шифроваться:\n")

encrypted_message = xor_encrypt_decrypt(message, key)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Расшифрованное сообщение:", decrypted_message)