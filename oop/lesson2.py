# Dunder methods or magic methods - __init__

country_names = {
    'Azerbaijan': [
        'azərbaycan', 'azerbaijan', 'azerbaycan',
    ],
    'Turkey': [
        'turkey', 'turkiye', 'türikye', 'türkiyə'
    ]
}


all_fin = []

class Person:
    class_name = 'Person'
    growth = 0.1
    year = 2024

    def __init__(
        self, name: str, surname: str, age: int, fin: str, salary: int
    ) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.country = None # Turkey, Azerbaijan
        self.fin = self.set_fin(fin) # Fin 7 simvol olur. Daxilinde l, o ve 0 olmaz!
        self.email = f'{name.lower()}.{surname.lower()}@gmail.com'
        self.salary = salary

    def get_fullname(self) -> str: # Method or Function 
        return '{} {}'.format(self.name, self.surname)
    
    def get_datas(self) -> str:
        return f'{self.name}-{self.surname}-{self.age}-{self.fin}'

    def set_country(self, country: str) -> None:
        if country in country_names.get('Azerbaijan'):
            self.country = 'Azerbaijan'
        elif country in country_names.get('Turkey'):
            self.country = 'Turkey'
        else:
            print('Daxil etidiyiniz ölkə tapılmadı. Default ölkə olaraq Azərbaycan təyin edildi.')
            self.country = 'Azerbaijan'

    def set_fin(self, fin: str) -> str:
        fin = fin.upper()
        if len(fin) != 7:
            raise ValueError('Daxil etdiyiniz məlumat doğru deyil. FİN daxilində 7 simvol olmalıdır.')
        elif 'L' in fin or '0' in fin or 'O' in fin:
            raise ValueError('Uyğunsuz simvol aşkar edildi!')
        elif fin in all_fin:
            raise ValueError('Daxil etdiyiniz FIN mövcuddur')
        all_fin.append(fin)
        return fin
    
    def increase_salary(self):
        self.salary += self.salary * self.growth
    
    @classmethod # ilk arqument olaraq class-i alir.
    def update_growth(cls, growth) -> None:
        cls.growth = growth

    @property # metod-u obyektin variable-i kimi davranmagini temin edir.
    def birth_year(self):
        return self.year - self.age
    
    # __str__

    def __str__(self) -> str:
        return self.name + ' ' + self.surname



# print(Person.class_name)

person1 = Person('Eli', 'Eliyev', 18, 'Azerbaycan', '1234567')
# person1.get_datas()
# person1.name

# person2 = Person('Veli', 'VEliyev', 20, 'Azerbaijan', '1234566')

# print(person1.email)
# print(person1.get_fullname())

# print(person2.name, person2.surname, person2.age, person2.fin)

# person3 = Person('Veli', 'Veliyev', 20, '1234566')
# person4 = Person('Samir', 'Veliyev', 20, '1234565')
# person5 = Person('Ilham', 'Veliyev', 20, '1234546')

# print(person3.country) # None

# person3.set_country('azerbaycan')
# Person.set_country(person3, 'azerbaycan')

# print(person3.country) # Azerbaijan

# print(person3.get_datas())
# # print(Person.get_datas(person3))

# print(person3.class_name)


person = Person('Ilham', 'Veliyev', 20, '1234546', 1200)
person1 = Person('Ilham', 'Veliyev', 20, '1232546', 1200)
person2 = Person('Ilham', 'Veliyev', 20, '1231546', 1200)

# print(person.salary)

# person.update_growth(0.2)

# person.increase_salary()

# print(person.salary)


# print(person.growth)
# print(person1.growth)
# print(person2.growth)

# person.update_growth(0.2)

# print(person.growth)
# print(person1.growth)
# print(person2.growth)

# print(person1.birth_year)


print(person)

