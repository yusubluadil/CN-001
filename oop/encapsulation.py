class Person:
    def __init__(
        self, name: str, surname: str, age: int, fin: str, year: str
    ) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.__fin = fin # Private
        self._birth_year = year # Protected

    def get_fin(self):
        return self.__fin
    
    def set_fin(self, value) -> None:
        self.__fin = value

    def __get_age(self):
        return self.age
    
    def check_obj_age(self):
        if self.__get_age() < 18:
            return False
        else:
            return True
    
    def _get_fullname(self):
        return self.name + ' ' + self.surname
    

    def fullname(self):
        return self._get_fullname()


obj = Person('Adil', 'Yusublu', 21, '1234567', '2002')

# print(obj.name)

# obj.name = 'Tural'

# print(obj.name)

# print(obj.get_fin())
# obj.fin = '7654321'
# obj.__fin = '7654321'
# print(obj.get_fin())
# print(obj.fin)
# print(obj.__fin)


# print(obj.get_fin())



# print(obj.get_fin())

# obj.set_fin('asd123c')

# print(obj.get_fin())


# print(obj._birth_year) # BELE CAGIRMAQ DUZGUN DEYIL !!!

print(obj.check_obj_age())
# print(obj.__get_age())

# print(help(Person))


print(obj._get_fullname()) # BELE CAGIRMAQ DUZGUN DEYIL !!!