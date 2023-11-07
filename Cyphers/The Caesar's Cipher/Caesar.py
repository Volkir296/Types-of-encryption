#Реализация алгоритма шифрования Цезаря
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A') #Выбор точки отсчета символов: заглавных или строчных
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset) #Смещение символов
            result += shifted_char #Запись результата
        else:
            result += char
    return result

#Захардкоженный пример
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(encrypted_text)  # Output: "Khoor, Zruog!"

#Пример с вводом информации пользователем
text = input("Введите фразу, которую хотите зашифровать: \n")
shift = int(input("Введите число, на которое хотите сместить символы: \n"))
encrypted_text = caesar_cipher(text, shift)
print(encrypted_text) 