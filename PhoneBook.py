# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

from PhoneBook_lib import *

phone_book = dict()

welcome()

while True:
    menu()
    choice = int(input("Введите режим работы: "))
    print("===== ===== =====")

    if choice == 1:
        show(phone_book)

    elif choice == 2:
        input_(phone_book)

    elif choice == 3:
        edit(phone_book)

    elif choice == 4:
        delete(phone_book)

    elif choice == 5:
        save(phone_book)

    elif choice == 0:
        print("До свидания!")
        print("===== ===== =====")
        break

    else:
        print("Ошибка")
        print("===== ===== =====")
        continue
