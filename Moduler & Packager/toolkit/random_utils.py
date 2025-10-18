import random
import string

def random_number(start, end):
    return random.randint(start, end)

def random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

def random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def random_otp():
    return ''.join(random.choice(string.digits) for _ in range(6))
