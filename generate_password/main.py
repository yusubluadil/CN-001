import datetime

from generate_password import generate_password

from logs import (
    add_logs,
    get_logs
)


while True:
    print(
        """
    1 -> Şifrə yarat
    2 -> LOG-lara bax
    q -> Çıxış et
    """
    )

    operation = input("Emeliyyati daxil edin: ")

    if operation == '1':
        pswd = generate_password()
        now = datetime.datetime.now()

        add_logs(now, pswd)

        print(pswd)
    elif operation == '2':
        print(get_logs())
    elif operation == 'q':
        print('Cixis edilir...')
        break
    else:
        print('Yanlis emeliyyat')
