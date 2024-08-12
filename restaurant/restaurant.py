"""

table_number, customer_name, time


class Reservation:
    all_table_count = 20
    reserved_table_count = 0
    ...

    
class Resturant:
    ...


"""


class Reservation:
    all_table_count = 20
    reserved_table_count = 0

    def __init__(self, table_number: int, customer_name: str, time: str) -> None:
        self.table_number = table_number
        self.customer_name = customer_name
        self.time = time

        Reservation.reserv_table()
    
    def check_table(self) -> None:
        if self.all_table_count < 1:
            raise Exception('Boş masa mövcud deyil!')

    @classmethod
    def reserv_table(cls) -> None:
        cls.all_table_count -= 1
        cls.reserved_table_count += 1

    @classmethod
    def unreserv_table(cls) -> None:
        cls.all_table_count += 1
        cls.reserved_table_count -= 1


class Resturant:
    def __init__(self) -> None:
        self.reservs = []
        print(Resturant)
    
    def add_reserv(self, table_number: int, customer_name: str, time: str) -> None:
        if Resturant.all_table_count:
            ...
    
    def list_reserv(self) -> None:
        for index, data in enumerate(self.reservs):
            print(f'{index} ---> {data.customer_name} - {data.table_number} - {data.time}')
    
    def remove_reserv(self, table_number: int) -> None:
        ...


restaurant = Resturant()

# obj1 = Reservation(1, 'asd', '12-12-2002')

