import random

def generate_rsa_keys(p, q):
    # Вычисление значения n
    
    n = p * q

    # Вычисление значения функции Эйлера от n
    phi_n = (p - 1) * (q - 1)

    # Выбор значения e
    e = choose_public_key(phi_n)

    # Вычисление значения d
    d = calculate_private_key(e, phi_n)

    # Возвращение открытого и закрытого ключей
    return (n, e), (n, d)

def generate_prime_number():
    # Генерация случайного числа
    num = random.randint(2**10, 2**11)

    # Проверка, является ли число простым
    while not is_prime(num):
        num += 1

    return num

def is_prime(num):
    # Проверка, является ли число простым
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def choose_public_key(phi_n):
    # Выбор значения e
    e = random.randint(2, phi_n - 1)

    # Проверка, является ли e взаимно простым с phi_n
    while gcd(e, phi_n) != 1:
        e += 1

    return e

def gcd(a, b):
    # Вычисление наибольшего общего делителя
    while b != 0:
        a, b = b, a % b
    return a

def calculate_private_key(e, phi_n):
    # Вычисление значения d
    d = pow(e, -1, phi_n)
    return d