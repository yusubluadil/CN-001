# import datetime

# from datetime import datetime as dt

# from rent_a_car.utils import (
#     LETTERS,
#     check_fin
# )



# a = 1

# data = ['salam', 'Python']
# new_data = ' '.join(data)

# print(new_data, 'CodeNext!', 'TechNext', sep='+++')


# name1 = input('Adinizi daxil edin: ')

# print(name1)


# List #
my_list = ['str', 50, True, [1, 2, 3]]
# my_list = [5, 10, 2, 50, 1259, 256, 512, 64]
# my_list.sort()
# my_list.append(6)
# print(my_list)

# a = my_list.pop(50)

# my_list.remove('str')
# my_list.clear()
# my_list.extend()
# my_list.count()


# Dict
# key: value
my_dict = {'name': 'Fatima'}
my_dict3 = {'surname': 'Jafarzadeh'}

my_dict2 = dict(name='Fatima')

# print(my_dict.get('surname', 'Jafarzadeh'))

# my_dict.keys()
# my_dict.values()
# my_dict.items()
# my_dict.update(my_dict3)
# my_dict.pop()
# my_dict.popitem()
# my_dict.setdefault('name', 'Milana')


# print(my_dict)


# Set
# Sirasiz, icindeki deyerler unikaldir, deyisilmiyen data tipdir
# my_set = {2, 1, 3, 4, 4, 4 ,5, 6 ,6, 'salam', 'salam'}

# print(my_set)


# Şərt və dövrlər #
# a = int(input('Bir eded daxil edin: '))
# b = int(input('Bir eded daxil edin: '))

# print(a is b)
# b = int(input('Bir eded daxil edin: '))

# if 0 < a < 100:
#     print('daxil etdiyiniz eded 1-100 araligindadir!')

# if 5 in range(1, 100):
#     print('example')

# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print(a, b)

# ==, !=, >, <, >=, <=, is, in, not in, is not


# numbers_1 = [1, 2, 3]

# numbers_2 = numbers_1

# numbers_3 = list((1, 2, 3))

# print(numbers_1 == numbers_2) True

# print(numbers_1 == numbers_3) True


# print(numbers_1 is numbers_2) True

# print(numbers_1 is numbers_3) False


# For and While

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# # print(i) # 4

# max_value = 10
# counter = 0
# while counter < max_value:
#     print(counter)
#     counter += 1


# name_datas = ['Izzet', 'Milana', 'Elchin', 'Konul', 'Fatime', 'Kenan', 'Tural']
# for index, value in enumerate(name_datas, 10):
#     print(index, value)


# Functions
# data = {'name': 'Milana'}

# def say_hi_with_name(*, name: str='Elchin') -> str:
#     return f'Salam {name}'

# print(say_hi_with_name(**data)) # name='Milana'


# def my_func(*args, **kwargs):
#     global some_datas
#     some_datas = [1, 2, 3, 4] # Local scope
#     print(some_datas)
#     print(args)
#     print(kwargs)

# my_func('Izzet', 'CodeNext', surname='Aghayev', age=20)
# print(some_datas)


# Exceptions

# try:
#     print(10 / 0)
# except (ValueError, ZeroDivisionError):
#     print('0-a bolmek olmaz!')
# finally:
#     print('Proqram sonlandi!')


# try:
#     print(variable)
# except Exception as e:
#     print(e)


# blocked_users = ['adil_444', 'izzet']
# user_input = input('User-i daxil edin: ')

# if user_input in blocked_users:
#     raise Exception('Daxil etdiyiniz user bloklanmisdir!')
# else:
#     print(user_input)
