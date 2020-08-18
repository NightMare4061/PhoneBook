# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

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


phone_book = dict()

print("*" * 41)
print("*** PhoneBook - телефонный справочник ***")
print("*" * 41)
print("Режим работы:")
print("1. Показать все записи")
print("2. Добавить запись")
print("3. Редактировать запись")
print("4. Удалить запись")
print("0. Выход")

choice = int(input("Введите режим работы"))

if choice == 1:
    print(phone_book)

elif choice == 2:
    tel = input("Введите номер телефона: ")
    value = input_data()
    phone_book[tel] = value

elif choice == 3:

elif choice == 4:

elif choice == 0:

else:
    print("Ошибка")


print(phone_book)
