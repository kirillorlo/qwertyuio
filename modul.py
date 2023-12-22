def reading():         
    data = 'phonebook.txt'   
    try:
        with open(data, 'r', encoding='utf-8') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print("Произошла ошибка:", e)
    

def find_contact_by_number():
    number_to_find = input("Введите номер телефона: ")
    try:
        with open('phonebook.txt', 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    name, number = line.strip().split(', ')
                    if number == number_to_find:
                        return f'Найден абонент с номером {number_to_find}: {name}'
                except ValueError:
                    continue
    except FileNotFoundError:
        return 'Файл не найден'
    return 'Абонент с таким номером не найден'



def add_contact():
    name = input("Введите имя: ")
    number = input("Введите номер телефона: ")
    with open('phonebook.txt', 'r+', encoding='utf-8') as f:
        lines = f.readlines()  

        for i, line in enumerate(lines):
            if line.strip() == "":
                lines[i] = f"{name}, {number}\n"
                f.seek(0)  
                f.writelines(lines)  
                print("Контакт успешно добавлен в справочник.")
        f.write(f"\n{name}, {number}")

        print("Контакт успешно добавлен в справочник.")
    

def delete_contact():
    last_name = input("Введите фамилию для удаления записи: ")
    lines = []
    deleted = False
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if last_name.lower() not in line.lower():
                lines.append(line)
            else:
                deleted = True
    if deleted:
        with open('phonebook.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)
        return f'Контакт {last_name} успешно удален из справочника.'
    else:
        return 'Контакт с такой фамилией не найден в справочнике.'