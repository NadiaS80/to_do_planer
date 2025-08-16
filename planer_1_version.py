class Action:
    def __init__(self, date, action,  done=False):
        self.date = date
        self.action = action
        self.done = done


class Planer:
    def __init__(self):
        self.planer = {}


    def add_action(self, task):
        if task.date not in self.planer:
            print(f'\nДаты {task.date} не было списке. Теперь она добавлена!')
            self.planer[task.date] = {}
            if not self.planer[task.date]:
                self.planer[task.date][1] = task.action
                print (f'\nНа {task.date} добавлено действие: {task.action}\n')
            else:
                max_key = max([key for key in self.planer[task.date].keys()])
                self.planer[task.date][max_key + 1] = task.action
                print (f'\nНа {task.date} добавлено действие: {task.action}\n')
        else:
            max_key = max([key for key in self.planer[task.date].keys()])
            self.planer[task.date][max_key + 1] = task.action
            print (f'\nНа {task.date} добавлено действие: {task.action}\n')


    def delete_action(self, user_date):
        try:
            if user_date in self.planer:
                print(f'\nНа {user_date} запланировано:')
                for num, plans in self.planer[user_date].items():
                    print(f'{num} - {plans}')
                print()
                number_action = int(input('Введи номер запланированного действия, которое ты хочешь удалить: '))
                if number_action in self.planer[user_date]:
                    deleted_action = self.planer[user_date][number_action]
                    del self.planer[user_date][number_action]
                    print(f'На дату {user_date} удалено действие: {deleted_action}')
                else:
                    print(f'Номера {number_action} ещё нет в списке.')
                list_numbers_and_plans = []
                for action in self.planer[user_date].values():
                    list_numbers_and_plans.append(action)
                self.planer[user_date].clear()
                max_key = 1
                for action in list_numbers_and_plans:
                    self.planer[user_date][max_key] = action
                    max_key += 1
 
            else:
                print(f'Даты {user_date} ещё нет в списке.')
        except ValueError:
            print(f'Нужно ввести значение, которое есть в списке действий\n')
        except KeyError:
            print("Ошибка: выбранной даты или действия нет в списке, или введено неверное значение.")


    def show_all_plans(self):
        if not self.planer:
            print(f'Планер пуст! Ты не добавил ни одного действия!\n')
        else:
            for date, numbers_and_plans in self.planer.items():
                print(f'\nНа {date} запланировано:')
                for nums, plans in numbers_and_plans.items():
                    print(f'{nums} - {plans}')
            print()



print('Привет! Я твой to_do list! Ты можешь добавлять в меня даты и действия, которые запланированы на какой либо день!\n')
user_planer = Planer()
a = 1
while a:
    try:
        user_choose_doing = int(input('Выбери действие:\n 1 - запланировать действие\n 2 - посмотреть запланированные дела\n 3 - удалить запланированное действие\n 4 - выйти из программы\n'))

        if user_choose_doing == 1:
            user_date = input('Введи дату, на котрорую хочешь запланировать действие в формате "ДД.ММ.ГГ": ')
            user_action = input(f'Введи действие, которое хочешь добавить на {user_date}: ')
            user_task = Action(user_date, user_action)

            user_planer.add_action(user_task)

        elif user_choose_doing == 2:

            user_planer.show_all_plans()
        elif user_choose_doing == 3:
            date_to_delete_action = input('Введи дату, из котророй хочешь удалить действие в формате "ДД.ММ.ГГ": ')

            user_planer.delete_action(date_to_delete_action)
        elif user_choose_doing == 4:
            print(f'Спасибо за работу! До встречи!')
            a = 0
        else:
            print(f'Нужно ввести значение от 1 до 3\n')
            continue
    except ValueError:
        print(f'Нужно ввести значение от 1 до 4\n')
        continue