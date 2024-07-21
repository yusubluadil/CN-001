# OOP -> Object Oriented Programming


# class adlarinin ilk herfi boyuk olmalidir!
# class adlari iki ve daha artiq sozden ibaret olarsa, bu zaman hemin sozlerin ilk herfleri boyuk olmalidir!


class person: # Bele yazilis yaxsi usul deyil
    pass


class Person:
    pass


a = int('1')
print(a)

my_lst = list()
print(my_lst)
print(type(my_lst))

person1 = Person()
print(person1)
print(type(person1))


class Person:
    # Konstruktor ve object yarandigi zaman ilk ise dusen func #
    def __init__(self) -> None:
        print('__init__ funksiyasi ise dusdu')

p2 = Person()
lst2 = list((1, 2, 3))


class Person:
    def __init__(self, name, surname, age) -> None:
        self.name = name # person3.name
        self.surname = surname # person3.name
        self.age = age # person3.name


# class Person:
#     def __init__(self, name, surname, age) -> None:
#         self.ad = name # person3.name
#         self.soyad = surname # person3.name
#         self.yas = age # person3.name


person3 = Person('Adil', 'Yusublu', 21)
print(person3.name, person3.surname, person3.age)
