import json


    
def input_surname():
      return input("Введите фамилию контакта: ").title()

def input_name():
      return input("Введите имя контакта: ").title()

def input_patronymic():
      return input("Введите отчество контакта: ").title()

def input_phone():
      return input("Введите телефон контакта: ")

def input_address():
      return input("Введите адрес(город) контакта: ").title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    contact = {
        "surname": surname,
        "name": name,
        "patronymic": patronymic,
        "phone": phone,
        "address": address
    }
    return contact


def add_contact():
    contact = create_contact()
    with open("phonebook.json", 'a', encoding='utf-8') as file:
        json.dump(contact, file)
        file.write("\n")

def print_contacts():
    with open("phonebook.json", 'r', encoding='utf-8') as file:
        contacts =  file.readlines()
    for n, contact in enumerate(contacts, 1):
        print(n, json.loads(contact))           

def search_contact():
    print(
            "Возможные варианты поиска:\n"
            "1. По фамилии\n"
            "2. По имени\n"
            "3. По отчеству\n"
            "4. По номеру телефона\n"
            "5. По адресу(городу)\n"
            )
    command = input("Введите вариант поиска: ")
    while command not in ("1", "2", "3", "4", "5"):
          print("Некорректный ввод!")
          command = input("Введите вариант поиска: ")
    i_command = int(command) - 1

    search =  input("Введите данные для поиска: ").title()
    with open("phonebook.json", 'r', encoding='utf-8') as file:
        contacts = file.readlines()
    
    for contact in contacts:
        contact_data = json.loads(contact)
        if search in contact_data[list(contact_data.keys())[i_command]]:
            print(contact_data)

def delete_contact():
    with open("phonebook.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        
        del data[number_row - 1]
        
        updated_data = [{'column2': row['column2'], 'column3': row['column3'], 'column4': row['column4'], 'column5': row['column5']} for row in data]
        
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(updated_data, file, ensure_ascii=False, indent=4)
        
        print("Строка успешно удалена!")

def change_contact():
      pass 

def import_contact():
      pass 


def interface():
    with open("phonebook.json", 'a', encoding='utf-8'):
        pass

    command = 0
    while command != "7":
        print(
            "Возможные варианты:\n"
            "1. Добавить контакт\n"
            "2. Вывести на экран\n"
            "3. Поиск контакта\n"
            "4. Удалить контакт\n"
            "5. Изменить контакт\n"
            "6. Перенести контакт\n"
            "7. Выход\n"
            )
        print()
        command = input("Введите вариант действия: ")
        while command not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Некорректный ввод!")
            command = input("Введите вариант действия: ")
        print()

        if command == "1":
            add_contact()
        elif command == "2":
            print_contacts()
        elif command == "3":
            search_contact()
        elif command == "4":
            delete_contact()
        elif command == "5":
            change_contact()
        elif command == "6":
            import_contact()        
        print()

interface()    
