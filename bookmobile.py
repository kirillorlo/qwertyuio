
#from modul import *

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

def reading():#1
    with open('phonebook.txt') as file:
        for i in file:
            print(i)

def find_contact_by_last_name(): #2
    with open('phonebook.txt') as file:
        family = input('Введите фамилию: ')
        for i in file:
            i = i.split(', ')
            if i[0] == family:
                print(i[1])         


def find_contact_by_number():#5
    with open('phonebook.txt') as file:
        number = int(input('Введите номер: '))
        family = {}
        for i in file:
            key, value = i.split(', ')
            family[key] = value.strip()

        for key, value in family.items():
            if value == str(number):
                print(f'Фамилия абонента - {key}')                

def change_phone_number(): #3
    number = int(input('Введите номер: '))
    with open('phonebook.txt', 'r+') as file:
        content = file.readlines()
        
        for i, line in enumerate(content):
            key, value = line.strip().split(', ')
            if value == str(number):
                print(key)
                new_number = int(input('Введите новый номер абонента: '))
                content[i] = f'{key}, {str(new_number)}\n'
                print('Номер изменён')
        file.seek(0)
        file.writelines(content)
        file.truncate()
        
           

           
menu_choice()


