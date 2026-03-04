import random
import string

def generate_password(length, use_numbers=False, use_symbols=False):

    if length < 4 or length > 12:
        raise ValueError("Length must be between 4 and 12")

    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    return password