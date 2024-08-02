# Abstraction -> Abstract method mutleq sekilde subclass-larda istifade olunmalidir!!!

from abc import (
    ABC,
    abstractmethod
)


class Car(ABC):
    """
    Car sinfi
    get_details() adli abstrakt metod var
    """

    def __init__(self, marka, model) -> None:
        self.marka = marka
        self.model = model

    # Asagida gosterilen metod mutleq sekilde subclass-larda yeniden teyin edilmelidir!!!
    # Teyin etmesek xeta mesaji verecek
    @abstractmethod
    def get_details(self):
        """ Abstract method """

        return {
            'marka': self.marka,
            'model': self.model
        }


class Sedan(Car):
    def __init__(self, marka, model, seat_count) -> None:
        super().__init__(marka, model)
        self.seat_count = seat_count
    
    def get_details(self):
        parent_datas = super().get_details()
        parent_datas['seat_count'] = self.seat_count
        return parent_datas

sedan_obj = Sedan('Opel', 'Astra', 5)

# sedan_obj.get_details()
print(sedan_obj.get_details())


print(help(Sedan))
