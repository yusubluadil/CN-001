from datetime import datetime


LETTERS = 'ÖĞIƏÇŞW'


def check_fin(fin: str) -> str:
    while True:
        if len(fin) != 7:
            print('FIN daxilinde 7 simvol olmalidir!!!')
            fin = input('FIN-i daxil edin: ')
        else:
            return fin


def check_plate(plate: str) -> str: # 00-XX-000
    splitted_plate = plate.split('-') # ['00', 'XX', '000']

    while True:
        if len(plate) != 9 or len(splitted_plate) != 3:
            print('Daxil etdiyiniz melumat dogru deyil')
            plate = input('Qeydiyyat nisanini daxil edin (00-XX-000): ')
        elif splitted_plate[0] == '00':
            print('Daxil etdiyiniz melumat dogru deyil')
            plate = input('Qeydiyyat nisanini daxil edin (00-XX-000): ')
        elif splitted_plate[1][0] in LETTERS:
            print('Daxil etdiyiniz melumat dogru deyil')
            plate = input('Qeydiyyat nisanini daxil edin (00-XX-000): ')
        elif splitted_plate[1][1] in LETTERS:
            print('Daxil etdiyiniz melumat dogru deyil')
            plate = input('Qeydiyyat nisanini daxil edin (00-XX-000): ')
        elif splitted_plate[2] == '000':
            print('Daxil etdiyiniz melumat dogru deyil')
            plate = input('Qeydiyyat nisanini daxil edin (00-XX-000): ')
        else:
            return plate


def check_date(date: str) -> str:
    year = int(datetime.now().year)

    while True:
        if date > year:
            print('Daxil etdiyiniz melumat dogru deyil!!!')
            date = int(input('İstehsal tarixi daxil edin: '))
        else:
            return date
