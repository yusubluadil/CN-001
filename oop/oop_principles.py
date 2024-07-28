#== OOP principles --> İnheritance, encapsulation, Polymorphism, Abstraction ==#


class Person:
    def __init__(
        self, name: str, surname: str, age: int, salary: int
    ) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        return self.name

# Boss, Developers, SMM

class Boss(Person):
    def __init__(self, name: str, surname: str, age: int, salary: int, workers = None):
        Person.__init__(self, name, surname, age, salary)
        if workers is not None:
            self.workers = workers
        else:
            self.workers = []
        
    
    def __str__(self) -> str:
        return Person.__str__(self)


boss1 = Boss('Xəyal', 'Quliyev', 35, 2500)

print(boss1.workers)


person1 = Person('Eli', 'Eliyev', 18, 500)
person2 = Person('Veli', 'VEliyev', 20, 700)

boss1.workers.append(person1)
boss1.workers.append(person2)

print(boss1.workers)
