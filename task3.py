# angle1 = abs(int(input('1-ci bucagi daxil edin: '))) #0
# angle2 = abs(int(input('2-ci bucagi daxil edin: '))) # 80
# angle3 = abs(int(input('3-cu bucagi daxil edin: '))) # 100


# sum_angle = angle1 + angle2 + angle3


# # kor, duz bucaqli, itibucaqli
# if sum_angle == 180:
#     if angle1 == 0 or angle2 == 0 or angle3 == 0:
#         print('0 dereceli bucaq daxil edile bilmez.')
#     elif angle1 == 90 or angle2 == 90 or angle3 == 90:
#         print('daxil etdiyiniz bucaqlar duzbucaqli ucbucaq yaradir.')
#     elif angle1 < 90 and angle2 < 90 and angle3 < 90:
#         print('Daxil etdiyiniz bucaqlar itibucaqli ucbucaq yaradir.')
#     else:
#         print('Daxil etdiyiniz bucaqlar korbucaqli ucbucaq yaradir.')
# else:
#     print('Daxil etdiyiniz bucaqlar üçbucaq yaratmır.')




# num = int(input('Bir reqem daxil edin: '))

# if num % 2 == 0:
#     print(f'{num} cut ededdir.')
# else:
#     print(f'{num} tek ededdir.')


# 25 5-in tam kv
# 37 hec bir ededin tam kv deyil
# print(25 ** 0.5)
# print(38 ** 0.5)

# num = int(input('Bir reqem daxil edin: '))


# if num < 0:
#     print('musbet eded daxil edin!')
# else:
#     num2 = num ** 0.5

#     if num2 % 1 == 0:
#         print('{} tam kvadratdir.'.format(int(num2)))
#     else:
#         print('hec bir ededin tam kv deyil.')



# num2 = int(num ** 0.5)


# if num == num2 ** 2:
#     print(num)
#     print(num2)
# else:
#     print('false')
#     print(num)
#     print(num2)


# pswd = input('Sifre daxil edin: ') # Password123@

# 12<, min 1 kicik herf, min 1 boyuk herf, min 1 reqem, @$%&*()!

# is == < in

# SYMBOLS = '@$%&*()!'

# if len(pswd) >= 12:
#     is_bigger_12 = True
# else:
#     is_bigger_12 = False


# is_upper = False
# is_lower = False
# is_numeric = False
# is_symbols = False

# for i in pswd:
#     if i.isupper():
#         is_upper = True
#     elif i.islower():
#         is_lower = True
#     elif i.isnumeric():
#         is_numeric = True
#     elif i in SYMBOLS:
#         is_symbols = True


# if (is_bigger_12 and is_upper and is_lower and is_symbols and is_numeric):
#     print('Guclu sifre')
# else:
#     print('zeif sifre')




username = input('Istifadeci adini daxil edin: ') # admin
pswd = input('Sifre daxil edin: ') # password123


# DB = {
#     1: {
#         'username': 'Adil',
#         'password': 'password455'
#     },
#     2: {
#         'username': 'admin',
#         'password': 'password123'
#     }
# }

# user_datas = DB.get(2)

# if username == user_datas.get('username') and pswd == user_datas.get('password'):
#     print('Giris ugurludur')
# else:
#     print('yanlis melumat')
