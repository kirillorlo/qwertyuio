
from modul import *

def menu_choice():
    print('1. Распечатать справочник')
    print('2. Найти телефон по фамилии')
    print('3. Изменить номер телефона')
    print('4. Удалить запись')
    print('5. Найти абонента по номеру телефона')
    print('6. Добавить абонента в справочник')
    print('7. Закончить работу с терминалом')

    choice = int(input('Введите номер операции: '))

    if choice == 1:
        print(reading())

    if choice == 2:
        print(find_contact_by_last_name())

    if choice == 3:
        print(change_phone_number())

    if choice == 4:
        print(delete_contact())

    if choice == 5:
        print(find_contact_by_number())

    if choice == 6:
        print(add_contact())

    return choice
    




# def change_phone_number():
#     with open('phonebook.txt', "r",encoding='utf-8') as file:
#         current_phone_number = file.read()
#     print("Текущий номер телефона:", current_phone_number)

#     number_to_change = input("Введите номер телефона, который вы хотите изменить: ")

#     if number_to_change == current_phone_number:
#         new_phone_number = input("Введите новый номер телефона: ")
#         with open('phonebook.txt', "w",encoding='utf-8') as file:
#             file.write(new_phone_number)
#         print("Номер телефона успешно изменен!")
        
#         new_name = input("Введите новое имя: ")
#         with open('phonebook.txt', "w",encoding='utf-8') as file:
#             file.write(new_name)
#         print("Имя успешно изменено!")
#     else:
#         print("Введенный номер телефона не совпадает с текущим номером.")

# change_phone_number()

        
menu_choice()