from CaesarFun import caesar_cipher, caesar_decipher

#Захардкоженный пример
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
decrypted_text = caesar_decipher(encrypted_text, shift)
print("Зашифрованное сообщение:",encrypted_text)  # Output: "Khoor, Zruog!"
print("Расшифрованное сообщение",decrypted_text)  # Output: "Hello, World!"


#Пример с вводом информации пользователем
text = input("Введите фразу, которую хотите зашифровать: \n")
shift = int(input("Введите число, на которое хотите сместить символы: \n"))
encrypted_text = caesar_cipher(text, shift)
decrypted_text = caesar_decipher(encrypted_text, shift)
print("Зашифрованное сообщение:",encrypted_text) 
print("Расшифрованное сообщение",decrypted_text) 