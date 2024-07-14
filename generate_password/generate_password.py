import random
import string


def generate_password() -> str:
    lowercase_letters = random.choices(string.ascii_lowercase, k=3)
    uppercase_letters = random.choices(string.ascii_uppercase, k=3)
    digits = random.choices(string.digits, k=3)
    punctuation = random.choices(string.punctuation, k=3)

    pswd = lowercase_letters + uppercase_letters + digits + punctuation
    random.shuffle(pswd)

    strong_password = ''.join(pswd)

    return strong_password
