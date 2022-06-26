import string, random

DIGITS = string.digits
LETTERS = string.ascii_letters
SAMPLES = '-?._!%#@$'

def generate_password(length, include_samples):
    password_bank = tuple(DIGITS + LETTERS)
    if include_samples:
        password_bank = tuple(DIGITS + LETTERS + SAMPLES)
    password = ''
    for i in range(length):
        password += random.choice(password_bank)
    return password

print(generate_password(8, False))
    