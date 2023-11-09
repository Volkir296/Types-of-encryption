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

#Реализация алгоритма расшифрования Цезаря
def caesar_decipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A') #Выбор точки отсчета символов: заглавных или строчных
            shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset) #Смещение символов
            result += shifted_char #Запись результата
        else:
            result += char
    return result