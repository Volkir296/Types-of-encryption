def Dec_to_Bin(Digit):
    Digit = int(bin(Digit)[2:])
    return Digit

def Bin_to_Dec(Bin_digit):
    Bin_digit = str(Bin_digit)
    Bin_digit = int(Bin_digit)
    return Bin_digit

def XOR_Fun(Num, Key):
    XOR_result = Num ^ Key
    return XOR_result