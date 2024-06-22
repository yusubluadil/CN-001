# loops: for and while


# name_list = ['Elcin', 'Resad', 'Emil', 'Tural']

# for name in name_list:
#     for letter in name:
#         print(letter)



# for letter in 'Code':
#     print(letter)


DB = {
    1: {
        'username': 'Adil',
        'password': 'password455'
    },
    2: {
        'username': 'admin',
        'password': 'password123'
    }
}

# for i in DB.get(2):
#     print(DB.get(2).get(i))


my_set = {1, 2, 3, 4, 5, 6, 'k', 30}
# print(my_set)

# for i in my_set:
#     print(i)



# range(start, end, step)   [::2]


lst = [5, 60, 24, 34, 21, 1, 78, 90, 100, 5697]

# for i in range(10, -2, -1):
    # print(i, end=', ') # 10, 9, 8




# Istifadecinin daxil etdiyi reqeme kimi butun ededlerin kv tapan proqram
# 1-100 butun cut ededleri tapan proqram. netice -> []
# verilmis bir siyahinin cemini tapan proqram. Istifadeci daxil edecek: '1,8,94,45'


#== Task 1 ==#

# num = int(input('Bir reqem daxil edin: '))

# for i in range(1, num + 1):
#     print(i ** 2)



#== Task 2 ==#


# for i in range(1, 101):
#     even_nums = []
#     if i % 2 == 0:
#         even_nums.append(i)

# print(even_nums)


# verilmis bir siyahinin cemini tapan proqram. Istifadeci daxil edecek: '1,8,94,45'

#== Task 3 ==#

# data = input('daxil et: ')

# data_list = data.split(',') # ['1', '2', '3']

# sum_data = 0

# for str_num in data_list:
#     int_num = int(str_num)
#     sum_data += int_num      # sum_data = sum_data + int_num

# print(sum_data)


# for i in range(11):
#     print(i)
# else:
#     print('Dovr bitdi')


# brak and continue


# fruits = ('alma', 'banan', 'heyva', 'armud')


# for fruit in fruits:
#     if fruit == 'heyva':
#         continue
#     print(fruit)


# for fruit in fruits:
#     print(fruit)
#     if fruit == 'banan':
#         break



# while

# counter = 0

# while True:
#     a = int(input('reqem daxil edin: '))
#     print(counter)
#     counter += 1

