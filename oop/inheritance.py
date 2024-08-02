#== İnheritance ==#

class Person:
    def __init__(
        self, name: str, surname: str, age: int, salary: int
    ) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_fullname(self):
        return self.name + ' ' + self.surname


class Developer(Person):
    def __init__(self, name: str, surname: str, age: int, salary: int, prog_lang: str) -> None:
        self.prog_lang = prog_lang
        # Person.__init__(self, name, surname, age, salary) # Tovsiye olunmur!!!
        super().__init__(name, surname, age, salary)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str: # representation
        return f'Developer({self.name}, {self.surname}, {self.age}, {self.salary}, {self.prog_lang})'
    
    def __add__(self, other):
        return self.name + ' ' + other.name

    def __len__(self):
        return len(f'{self.name} {self.surname}')


dev1 = Developer('Eli', 'Veliyev', 25, 1200, 'Python')
dev2 = Developer('Veli', 'Veliyev', 25, 1200, 'C#')
dev3 = Developer('Elnure', 'Veliyeva', 25, 500, 'Java')

print(1 + 5 + 45 + 20)
# print(repr(dev1))
# print(str(dev1))
print(dev1 + dev2)


data = 'Python'
print(len(data))


print(len(dev3))


# getter, setter


class Employee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = 'Mehemmed'



dev4 = Employee('Xeyal')

print(dev4.name)
dev4.name = 'adil'

print(dev4.name)




# print(dev1.name)
# print(dev1.prog_lang)

# print(help(Developer))


# Boss, Developer, SMM

# class Boss(Person):
#     def __init__(self, name: str, surname: str, age: int, salary: int, workers = None):
#         Person.__init__(self, name, surname, age, salary)
#         if workers is not None:
#             self.workers = workers
#         else:
#             self.workers = []
        
    
#     def __str__(self) -> str:
#         return Person.__str__(self)


# boss1 = Boss('Xəyal', 'Quliyev', 35, 2500)

# print(str(boss1))

# boss1.change_class_name()


# person1 = Person('Eli', 'Eliyev', 18, 500)
# person2 = Person('Veli', 'VEliyev', 20, 700)

# boss1.workers.append(person1)
# boss1.workers.append(person2)

# print(boss1.workers)
