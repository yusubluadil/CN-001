# Tuple


# my_tpl = (1, 2, 3, 4)

# print(type(my_tpl))


# # my_tpl = 1, 2, 3, 4


# # print(type(my_tpl))


# a = (1)

# print(type(a))


# b = 5,

# print(type(b))



# str1 = 'Adil'

# # del my_tpl
# # del str1



# my_tpl = ('a', 'b', 'c', 'g', 'd', 'e', 'f', 'g', '5', 'g')


# print(my_tpl)


# print(my_tpl.count('g'))


# print(my_tpl.index('g'))


# print(len(my_tpl))


# a = list([1, 1, 5])

# b = tuple((1, 2, 3))


# print(a)
# print(b)



# my_tpl = (1, 2, 3, 4)

# 2
# # Adil




# Dictionary




# my_dict = {'name': 'Elçin', 'age': 21, 'gender': 'Male'} # {'key': 'value'}

# birth_year = 2002

# # my_dict['name'] = 25

# my_dict['birth_year'] = birth_year

# del my_dict['age']


# my_dict = dict(name='Elchin', age=21, gender='male')

# # my_dict.clear()

# # print(my_dict)


# copied_dict = my_dict.copy()

# copied_dict['surname'] = 'Aliyev'

# print(copied_dict, my_dict, sep=' <---> ')







# keys_list = ['k1', 'k2', 'k3', 'k4']
# default_value = 15

# empty_dict = {}

# new_dict = dict.fromkeys(keys_list, default_value)


# print(new_dict)






# my_dict = dict(list=[1, 2, 3], age=21, gender=1,2,3)

# # my_dict['surname']
# print(my_dict.get('surname', 'Aliyev')) # Aliyev


# print(my_dict)



# my_dict = dict(my_dict2=dict(k1=12, k2=13) , age=21, gender='male', name='Adil')

# print(my_dict)


# dict_items = list(my_dict.items())

# print(dict_items[1][1])



# print(list(my_dict.keys()))

# print(tuple(my_dict.values()))


# # del my_dict['name']


# deleted_item = my_dict.pop('name', 'Aliyev')
# print(deleted_item)


# print(my_dict)

# print(deleted_item)



# dct = {'names': ['elnur', 'adil']}


# lst = dct.get('names')

# del lst[-1]

# print(dct)





# print(my_dict.popitem())

# print(my_dict)

# a = {'surname': 'Aliyev'}

# my_dict.update(a)

# print(my_dict)
# print(a)

my_dict = dict(name='Ilham', age=21, gender='male')


print(my_dict)

a = my_dict.setdefault('age', 30)
b = my_dict.setdefault('surname', 'Ehmedli')

print(my_dict)



print(a, b)
