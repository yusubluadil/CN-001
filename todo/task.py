"""

Tapsirigin tehvil verilmesi - 06-08-2024 - Icra edildi

class Task:
    ...


class ToDo:
    ...

"""


class Task:
    is_completed = False

    def __init__(self, title: str, time: str) -> None:
        self.title = title
        self.time = time # DateTime object olaraq saxla
        self.is_completed = False
    
    def change_status(self) -> None:
        if self.is_completed:
            self.is_completed = False
        else:
            self.is_completed = True
    
    def __str__(self) -> str:
        return self.title


class ToDo:
    def __init__(self) -> None:
        self.todo_list = []

    def add_task(self, task_obj: Task) -> None:
        self.todo_list.append(task_obj)

    def add_multiple_task(self, *args) -> None:
        for i in args:
            self.todo_list.append(i)

    def list_tasks(self) -> None:
        for index, i in enumerate(self.todo_list):
            print(index, ' ---> ', i)

    def remove_task(self, index: int) -> None:
        self.todo_list.pop(index) # ToDo: Eger index olmasa xeta verir. (Edit Bug)

    def remove_multiple_task(self, *args) -> None:
        # Check #
        for i in args:
            if not isinstance(i, int):
                raise Exception('zehmet olmasa integer data daxil edin!')
            
            if i > len(self.todo_list):
                raise Exception('Daxil etdiyiniz index movcud deyil!')

        lst_args = list(args)
        # lst_args.sort(reverse=True)

        for i in lst_args:
            self.todo_list.pop(i)

    def filter_status(self, is_completed: bool) -> None:
        for index, i in enumerate(self.todo_list):
            if i.is_completed == is_completed:
                print(index, ' ---> ', i.title, i.is_completed)


todo = ToDo()

# print(isinstance(todo, ToDo))


task1 = Task('Python proyektin tehvil verilmesi', '14-08-2024 23:00')
task2 = Task('Imtahana hazirlasmaq', '15-08-2024 18:00')
task3 = Task('Server deployment', '16-08-2024 02:00')

# print(task1.is_completed)
# task1.change_status()
# print(task1.is_completed)


todo.add_multiple_task(task1, task2, task3)
# todo.list_tasks()
# print('----------------------------------------------------')
# todo.remove_task(0)
# todo.list_tasks()

# task3.change_status()
# print('----------------------------------------------------')
# todo.list_tasks()


# todo.remove_task(6)

# todo.filter_status(True)


todo.remove_multiple_task(0, 1, 2)

