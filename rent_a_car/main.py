from utils import (
    check_fin,
    check_plate,
    check_date
)

from add_car import add_car


#== Login ==#
USERNAME = 'orxan_rent_85'
PSWD = 'yBZ0eNped3eX27b'
LOGIN_STATUS = False

def login() -> bool:
    global LOGIN_STATUS

    username = input('Username-nizi daxil edin: ')
    pswd = input('Sifrenizi daxil edin: ')

    if username is not None and pswd is not None:
        if username == USERNAME and pswd == PSWD:
            print('Muveffeqiyyetle daxil oldunuz')
            LOGIN_STATUS = True
            return True
        else:
            print('Istifadeci adi ve ya sifre yanlisdir!')
            return False
    else:
        print('istifadeci adi ve ya sifre mutleq daxil edilmelidir!')
        return False

#== Login ==#


#== Main ==#
while True:
    # if not LOGIN_STATUS:
    #     login()
    # else:
    print("""
    1 -> Avtomobil elave et
    2 -> Butun avtomobiller # Sirlama, Filter
    3 -> Avtomobil detallarina bax
    4 -> Avtomobil melumatlari yenile
    5 -> Avtomobil sil
    6 -> Icareye ver
    0 -> Cixis
""")
    
    try:
        operation = int(input("Emeliyyati daxil edin: "))
    except:
        print('Daxil etdiyiniz emeliyyat dogru deyil!!!')
        continue

    if operation == 1:
        marka = input('Markani daxil edin: ')
        model = input('Modeli daxil edin: ')

        while True:
            try:
                date_of_production = int(input('İstehsal tarixi daxil edin: '))
                checked_date_of_production = check_date(date_of_production)

                march = int(input('Yurusu daxil edin: '))
                engine_volume = float(input('Muherrik hecmi daxil edin: '))
                price = int(input('Qiymeti daxil edin: '))
            except:
                print("Dogru melumatlar daxil edin!!!")
                continue
            else:
                break
            
        color = input('Rengi daxil edin: ')
        plate = input('Qeydiyyat nisanini daxil edin (00-XX-000): ').upper()
        checked_plate = check_plate(plate)

        owner_fullname = input('Avtomobil sahibinin ad və soyadını daxil edin: ')
        fin = input('Avtomobil sahibinin FIN-in daxil edin: ').upper()
        checked_fin = check_fin(fin)

        car_data = add_car(
            marka=marka, model=model, date_of_production=checked_date_of_production,
            march=march, engine_volume=engine_volume, price=price,
            color=color, plate=checked_plate, owner_fullname=owner_fullname,
            fin=checked_fin
        )

    elif operation == 2:
        ...
    elif operation == 3:
        ...
    elif operation == 4:
        ...
    elif operation == 5:
        ...
    elif operation == 6:
        ...
    elif operation == 0:
        print('Proqramdan cixis edilir...')
        break
    else:
        print('Daxil etdiyiniz emeliyyat dogru deyil!!!')
#== Main ==#
