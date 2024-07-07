"""

admin
username = adil_444
pswd = adil2002

1 -> isci elave et
2 -> isci sil
3 -> butun isciler
4 -> isci melumatlarini yenile
5 -> isci detallari

"""

# login, create_worker, delete_worker, list_workers, update_worker, detail_worker, logout

USERNAME = 'adil_444'
PSWD = 'adil2002'

DB = {}

# Elave funcs start #

def check_fin(fin=None) -> bool:
    all_datas = DB.values()
    for data in all_datas:
        if fin == data.get('fin'):
            print('Daxil etdiyiniz FIN DB-da movcuddur!')
            return True
        else:
            return False

def check_username(username=None) -> bool:
    all_datas = DB.values()
    for data in all_datas:
        if username == data.get('username'):
            print('Daxil etdiyiniz username DB-da movcuddur!')
            return True
        else:
            return False

def generate_id() -> int:
    all_ids = list(DB.keys())
    if all_ids == []:
        return 1
    else:
        return all_ids[-1] + 1

# Elave funcs end #
login_status = False

def login() -> bool:
    global login_status

    username = input('Username-nizi daxil edin: ')
    pswd = input('Sifrenizi daxil edin: ')

    if username is not None and pswd is not None:
        if username == USERNAME and pswd == PSWD:
            print('Muveffeqiyyetle daxil oldunuz')
            login_status = True
            return True
        else:
            print('Istifadeci adi ve ya sifre yanlisdir!')
            return False
    else:
        print('istifadeci adi ve ya sifre mutleq daxil edilmelidir!')
        return False

def create_worker(
    *,
    name=None,
    surname=None,
    age=0,
    fin=None, # unique
    username=None, # unique
    pswd=None,
):
    id = generate_id()

    data = {
        'name': name,
        'surname': surname,
        'age': age,
        'fin': fin,
        'username': username,
        'password': pswd
    }

    DB[id] = data

def delete_worker(*, id=0):
    if id in DB:
        DB.pop(id)
        print('isci muveffeqiyyetle silindi')
    else:
        print('daxil etdiyiniz ID-ye uygun isci tapilmadi!')

def list_workers():
    for id, data in DB.items():
        print(id, '---', data)

def update_worker():
    ...

def detail_worker(*, id):
    data = DB.get(id)
    if data is not None:
        print(data)
    else:
        print('daxil etdiyiniz ID-ye uygun isci tapilmadi!')


while True:
    if not login_status:
        login()
    else:
        print("""
            1 -> isci elave et
            2 -> isci sil
            3 -> butun isciler
            4 -> isci melumatlarini yenile
            5 -> isci detallari
            0 -> Cixis et
        """)
        
        operation = input('emeliyyati daxil edin: ')

        if operation == '1':
            name = input('adi daxil edin: ')
            surname = input('soyadi daxil edin: ')
            age = int(input('yasi daxil edin: '))
            fin = input('Fin-i daxil edin: ').upper()
            while check_fin(fin):
                fin = input('fin daxil edin: ')
            
            username = input('username-i daxil edin: ')
            while check_username(username):
                username = input('username daxil edin: ')

            pswd = input('sifren-i daxil edin: ')

            create_worker(name=name, surname=surname, age=age, fin=fin, pswd=pswd, username=username)
        elif operation == '2':
            id = int(input('id-ni daxil edin: '))

            delete_worker(id=id)
        elif operation == '3':
            list_workers()
        elif operation == '4':
            ...
        elif operation == '5':
            id = int(input('id-ni daxil edin: '))

            detail_worker(id=id)
        elif operation == '0':
            print('proqramdan cixis edilir!')
            break
        else:
            print('Yanlis emeliyyat!')



# FIN-in 7 simvoldan ibaret olmasini temin edin!
# Sifrenin minimum uzunlugu 8 simvol olmalidir! 
# 4-cu bendi tamamlayin

# filter tetbiq olunsun -> yas, name, surname
#     yas daxil edildiyi zaman hemin daxil edilen yasdan boyuk olan istifadeciler gelsin
#     name daxil edildiyi zaman hemin ada uygun olan istifadeciler cixsin
#     surname daxil edildiyi zaman hemin soyada uygun olan istifadeciler cixsin
