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
                print(f'Номер {family} - {i[1]}')         


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


def delete_contact(): #4
    data = input('Введите фамилию: ')
    
    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()
    
    with open('phonebook.txt', 'w') as file:
        for line in lines:
            key, value = line.strip().split(', ')
            if key != data:
                file.write(f'{key}, {value}\n')
        return 'Номер удален' 

def add_contact():
    data_name = input('Введите фамилию: ') 
    data_number = int(input('Введите номер: '))  
    with open('phonebook.txt', 'a') as file:
        file.write(f'{data_name}, {data_number}\n')
        
        return 'Абонент успешно добавлен!)'
