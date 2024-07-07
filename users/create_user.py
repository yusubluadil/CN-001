from datetime import (
    datetime
)

from db import DB

from utils import generate_id


today = datetime.today()


def create_user(*, name: str=None, surname: str=None, created_at: str=None) -> dict:
    if created_at == '':
        created_at = today
    else:
        flag = True
        while True:
            try:
                if flag:
                    created_at = datetime.strptime(created_at, '%d-%m-%Y') # 14.11.2024
                    if created_at > today:
                        print('Gelecek tarix daxil edile bilmez!')
                    else:
                        break
                created_at = input('Ise daxil oldugu tarix [GG-AA-IIII] (Bos kecile biler): ')
                flag = True
            except ValueError:
                flag = False
                print('Daxil etdiyiniz format düzgün deyil')

    id = generate_id()

    data = {'name': name, 'surname': surname, 'created_at': created_at}
    DB[id] = data

    return data
