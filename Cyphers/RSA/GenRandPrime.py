import random

def generate_random_prime():
    start, end = 1, 100 #Диапазон
    prime = random.randint(start, end)
    while not is_prime(prime):
        prime = random.randint(start, end)
    return prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def exit_gen():
    digit = generate_random_prime()
    return digit