# Sets and conditions #


# my_set = {'k1', 'k2', 'k3', 'k4', 'k5', 'k6'} # Sirasiz
# my_tuple = ('k1', 'k2', 'k3', 'k4', 'k5', 'k6') # Sirali

# # set()


# # print(my_set)
# # print(my_tuple)

# del my_set


# my_set = {'k1', 'k6', 'k2', 'k3', 'k6', 'k4', 'k5', 'k6', True, 1, False, 0}
# my_tuple = ('k1', 'k6', 'k2', 'k3', 'k6', 'k4', 'k5', 'k6', True, 1, False, 0)

# print(my_set)
# # print(my_tuple)



# my_set.add('k7')
# # my_set.clear()
# copied_set = my_set.copy()

# my_set.add(8)

# # print(my_set)
# # print(copied_set)




# # print)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# # x.difference(y)

# # print(x)

# # x.difference_update(y)

# # print(x)


# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}

# # c = y.issuperset(x)

# # print(c)

# # c = x.pop()
# # x.remove("a")

# # print(x)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# a = 'CodeNext'
# empty_set = set()


# z = x | {123}

# print(z)








# Conditions #

# if elif else


# 5==5 != < > <= >=

# in, not in, is --> ==, is not --> !=


# a = [1, 2, 3]
# b = [1, 2, 3]


# print(2 is 2.0)
# print(2 == 2.0)


my_str = 'Code'

if 'C' not in my_str:
    print('C movcuddur')
elif 'o' not in my_str:
    print('o movcuddur')
elif 'd' in my_str:
    print('d movcuddur')
else:
    print('herf yoxdur')


# if 5 <= 5:
#     print('5 5-den kicikdir ve ya beraberdir')




# 1. istifadeci 3 dene reqem daxil edir. En boyuk olani ekrana yazdir.


# num1 = int(input('1-ci rəqəm: '))
# num2 = int(input('2-ci rəqəm: '))
# num3 = int(input('3-cu rəqəm: '))

# if (num1 > num2):
#     greater_num = num1
# else:
#     greater_num = num2

# if (num3 > greater_num):
#     print(f'Ən böyük ədəd: {num3}')
# else:
#     print(f'Ən böyük ədəd: {greater_num}')




"""
2. istifadeci sagirdin adini, yasini, sinfini, 3 fenn ve onlara uygun qiymeti daxil edir.
   1 --> butun melumatlar
   2 --
"""


# name = input('ad: ')
# age = input('yas: ')
# class_name = input('sinif: ')

# subject1 = input('fenn1: ')
# point1 = int(input('qiymet1: '))
# subject2 = input('fenn2: ')
# point2 = int(input('qiymet2: '))
# subject3 = input('fenn3: ')
# point3 = int(input('qiymet3: '))

# data = {
#     name: {
#         'age': age,
#         'class': class_name,
#         'subjects_and_points': [
#             (subject1, point1),
#             (subject2, point2),
#             (subject3, point3),
#         ]
#     }
# }



# operation = int(input('əməliyyatı daxil edin: '))

# if True:
#     ...



# if (operation == 1):
#     print(data)
# elif (operation == 2):
#     name_data = data.get(name)
#     listed_keys = list(data.keys())

#     print(listed_keys[0], name_data.get('age'), name_data.get('class'), sep='\n')
# elif (operation == 3):
#     avg = (point1 + point2 + point3) / len(data.get(name).get('subjects_and_points'))
#     print(data.get(name), )
# else:
#     print('Invalid')



# and, or 

# 1. istifadeci 3 dene reqem daxil edir. En boyuk olani ekrana yazdir.

num1 = 3
num2 = 4
num3 = 5

# True = 1, False = 0
# and --> *
# or --> +

# if (num1 >= num2 and num1 >= num3 and or):
#     print(num1)
# elif (num2 >= num1 or num2 >= num3 or):
#     print(num2)
# else:
#     print(num3)

a = 5 + 5

a = a - 1
a -= 1
a += 1


print()

# nested, one line


i = -5

if i != 0:
    if i > 0:
        print("Positive")
    else:
        print("Negative")
    
else:
    print("Zero")



if True:
    ...

if True:
    ...


if True:
    ...
elif True:
    ...

num = int(input('reqem daxil edin: '))


# if (num > 0):
#     print('a')
# else:
#     print('b')


# if (num > 0): print('a')
# else: print('b')


print('a') if num > 0 else print('b')


print('a' if num > 0 else 'b')


_asdd = None

asdd = _asdd

__asd = None

# if (5 < 6):
#     print('asd')



