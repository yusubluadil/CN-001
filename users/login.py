EMAIL = 'a@gmail.com'
PASSWORD = 'asd'


def login(email: str=None, password: str=None) -> bool:
    if email == EMAIL and password == PASSWORD:
        return True
    return False
