import json

from logger import*

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