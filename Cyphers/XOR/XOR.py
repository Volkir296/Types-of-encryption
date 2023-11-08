def XOR(Num, Key):
    Num = int(bin(Num)[2:])
    Key = int(bin(Key)[2:])
    bin_result = Num ^ Key
    dec_result = str(bin_result)
    dec_result = int(dec_result,2)
    print(dec_result)
 


    
num = int(input())
key = int(input())

XOR(num,key)

'''
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


# Пример использования с помощью данных, вводимых пользователем
message = input("Введите фразу, которую хотите зашифровать:\n")
key = input("Введите фразу-ключ, которой фраза будет шифроваться:\n")

encrypted_message = xor_encrypt_decrypt(message, key)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Расшифрованное сообщение:", decrypted_message)
'''