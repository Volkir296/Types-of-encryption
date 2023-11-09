#GUI
def Dec_to_Bin(Digit):
    Digit = int(bin(Digit)[2:])
    return Digit

def Bin_to_Dec(Bin_digit):
    Bin_digit = str(Bin_digit)
    Bin_digit = int(Bin_digit,2)
    return Bin_digit

def XOR_Fun(Num, Key):
    XOR_result = Num ^ Key
    return XOR_result

#Console
#Работает с текстом 
#проблема в кодировке но работает (вывод невидимых символов)
def xor_encrypt_decrypt(message, key):
    encrypted = ""
    for i in range(len(message)):
        # Применяем операцию XOR между символом сообщения и соответствующим символом ключа
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted