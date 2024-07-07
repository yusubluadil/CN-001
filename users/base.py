import login
from create_user import create_user
from detail_user import detail_user


while True: # Login
    email = input('Email daxil edin: ')
    password = input('Şifrə daxil edin: ')

    checked = login.login(email=email, password=password)
    if checked:
        print('Müvəffəqiyyətlə daxil oldunuz!')
        break
    print('Sifre ve ya email yanlisdir!')



while True: # Operations
    print("""
    1 -> Create User
    2 -> Detail User
    3 -> Exit
""")
    operation = input('Emeliyyati daxil edin: ')

    if operation == '1':
        name = input('Adi daxil edin: ')
        surname = input('Soyadi daxil edin: ')
        created_at = input('Ise daxil oldugu tarix [GG-AA-IIII] (Bos kecile biler): ')

        user = create_user(name=name, surname=surname, created_at=created_at)
        print(user)
    elif operation == '2':
        id = int(input('ID-ni daxil edin: '))
        print(detail_user(id=id))
    elif operation == '3':
        print('Proqramdan cixis edilir...')
        break
    else:
        print('Yanlis emeliyyat daxil etdiniz!')
