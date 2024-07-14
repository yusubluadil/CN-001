"""
1. Oldugunuz qovlugun adini ekrana yazdiran funksiya

2. Yeni folder yaradin

3. Mövcud olan bir faylın adını dəyişin

4. İstifadəçinin daxil etidyi fayl adına uyğun faylı silin

5. Qovluqda olan bütün faylların siyahısını çıxarın.

"""

import os


#== 1. Oldugunuz qovlugun adini ekrana yazdiran funksiya ==#
def get_current_directory() -> str:
    return os.getcwd()

print(get_current_directory())


#== 2. Yeni folder yaradin ==#
def create_folder(folder_name: str=None) -> None:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        print('Daxil etdiyiniz ada uyğun qovluq mövcuddur!!!')

folder_name = input('Yaratmaq istədiyiniz qovluq adını daxil edin: ')

create_folder(folder_name)


#== 3. Mövücud olan bir faylın adını dəyişin ==#
def rename_folder(current_dir_name: str=None, new_dir_name: str=None) -> str:
    if os.path.exists(current_dir_name):
        os.rename(current_dir_name, new_dir_name)
        return f'{current_dir_name} adlı fayl {new_dir_name} adı ilə dəyişdirildi!'
    else:
        return f'Daxil etdiyiniz {current_dir_name} adlı fayl mövcud deyil!'

current_dir_name = input("Dəyişiləcək fayl adını daxil edin: ")
new_dir_name = input("Yeni fayl adını daxil edin: ")

print(rename_folder(current_dir_name, new_dir_name))


#== 4. İstifadəçinin daxil etidyi fayl adına uyğun faylı silin ==#
def remove_file(file_name) -> str:
    if os.path.exists(file_name):
        os.remove(file_name)
        return f'{file_name} adlı fayl müvəffəqiyyətlə silindi!'
    else:
        return f'Daxil etdiyiniz {file_name} adlı fayl mövcud deyil!'

file_name = input("Silmək istədiyini fayl adını daxil edin: ")

print(remove_file(file_name))


#== 5. Qovluqda olan bütün faylların siyahısını çıxarın ==#
def list_dir_files() -> list[str]:
    return os.listdir()

print(list_dir_files())
