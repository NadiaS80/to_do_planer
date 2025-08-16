to_do_planer = {}



# def add_date():
#     user_date = input('Введи дату, которую хочешь добавить в формате "ДД.ММ.ГГ": ')
#     if user_date not in to_do_planer:
#         to_do_planer[user_date] = {}
#         print(f'\nДата {user_date} добавлена в планер!\n')
#     else:
#         print(f'\nДата {user_date} уже есть в списке!\n')



def add_action():
    user_date = input('Введи дату, на котрорую хочешь запланировать действие в формате "ДД.ММ.ГГ": ')
    if user_date not in to_do_planer:
        print(f'\nДаты {user_date} не было списке. Теперь она добавлена!\n')
        to_do_planer[user_date] = {}
        user_action = input(f'Введи действие, которое хочешь добавить на {user_date}: ')
        if not to_do_planer[user_date]:
            to_do_planer[user_date][1] = user_action
            print (f'\nНа {user_date} добавлено действие: {user_action}\n')
        else:
            max_key = max([key for key in to_do_planer[user_date].keys()])
            to_do_planer[user_date][max_key + 1] = user_action
            print (f'\nНа {user_date} добавлено действие: {user_action}\n')
    else:
        user_action = input(f'Введи действие, которое хочешь добавить на {user_date}: ')
        if not to_do_planer[user_date]:
            to_do_planer[user_date][1] = user_action
            print (f'\nНа {user_date} добавлено действие: {user_action}\n')
        else:
            max_key = max([key for key in to_do_planer[user_date].keys()])
            to_do_planer[user_date][max_key + 1] = user_action
            print (f'\nНа {user_date} добавлено действие: {user_action}\n')




def delete_action():
    try:
        user_date = input('Введи дату, из котророй хочешь удалить действие в формате "ДД.ММ.ГГ": ')
        a = 0
        for date, numbers_and_plans in to_do_planer.items():
            if date == user_date:
                a = 1
                print(f'\nНа {date} запланировано:')
                for num, plans in numbers_and_plans.items():
                    print(f'{num} - {plans}')
                print()
                number_action = int(input('Введи номер запланированного действия, которое ты хочешь удалить: '))

                if number_action in numbers_and_plans:
                    deleted_action = numbers_and_plans[number_action]
                    del numbers_and_plans[number_action]
                    print(f'На дату {user_date} удалено действие: {deleted_action}')
                else:
                    print(f'Номера {number_action} ещё нет в списке.')

            list_numbers_and_plans = []
            for action in numbers_and_plans.values():
                list_numbers_and_plans.append(action)
            numbers_and_plans.clear()
            max_key = 1
            for action in list_numbers_and_plans:
                to_do_planer[user_date][max_key] = action
                max_key += 1

        if not a:
            print(f'Даты {user_date} ещё нет в списке.')
    except ValueError:
        print(f'Нужно ввести значение, которое есть в списке действий\n')
    except KeyError:
        print("Ошибка: выбранной даты или действия нет в списке, или введено неверное значение.")



def user_choose_doing():
    while True:
        try:
            user_choose_doing = int(input('Выбери действие:\n 1 - запланировать действие\n 2 - посмотреть запланированные дела\n 3 - удалить запланированное действие\n 4 - выйти из программы\n'))
            # if user_choose_doing == 1:
            #     return add_date()
            if user_choose_doing == 1:
                return add_action()
            elif user_choose_doing == 2:
                show_all_plans()
            elif user_choose_doing == 3:
                delete_action()
            elif user_choose_doing == 4:
                print(f'Спасибо за работу! До встречи!')
                return 0
            else:
                print(f'Нужно ввести значение от 1 до 3\n')
                continue
        except ValueError:
            print(f'Нужно ввести значение от 1 до 5\n')
            continue




def show_all_plans():
    if not to_do_planer:
        print(f'Планер пуст! Ты не добавил ни одного действия!\n')
    else:
        for date, numbers_and_plans in to_do_planer.items():
            print(f'\nНа {date} запланировано:')
            for nums, plans in numbers_and_plans.items():
                print(f'{nums} - {plans}')
        print()



print('Привет! Я твой to_do list! Ты можешь добавлять в меня даты и действия, которые запланированы на какой либо день!\n')
a = 1
while a:
    work = user_choose_doing()
    if work == 0:
        a = 0