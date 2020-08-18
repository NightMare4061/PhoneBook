def input_data():
    temp = list()
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    address = input("Введите адрес: ")
    temp.append(last_name)
    temp.append(first_name)
    temp.append(patronymic)
    temp.append(address)
    return temp

def welcome():
    print("*" * 41)
    print("*** PhoneBook - телефонный справочник ***")
    print("*" * 41)

def menu():
    print("Режим работы:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("0. Выход")
    print()
