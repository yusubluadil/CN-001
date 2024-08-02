class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def speak(self) -> str:
        return ''


class Wolk(Animal):
    def speak(self) -> str:
        return 'Woof!'


class Cat(Animal):
    def speak(self) -> str:
        return 'Miyauww!'


obj1 = Animal('Mamont')
obj2 = Wolk('W1')
obj3 = Cat('Mestan')


print(obj1.speak())
print(obj2.speak())
print(obj3.speak())

# Polymorphism -> Eyni adli metodlarin muxtelif neticelerine deyilir!
