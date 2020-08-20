from tkinter import *
import os

phone_book = dict()
tel_list = list()

def clear():
    input_tel.delete(0, END)
    input_last_name.delete(0, END)
    input_first_name.delete(0, END)
    input_patronymic.delete(0, END)
    input_address.delete(0, END)


def add():
    tel = input_tel.get()
    if tel in phone_book:
        label_info.config(text="Такой номер уже существует")
    else:
        value = list()
        value.append(input_last_name.get())
        value.append(input_first_name.get())
        value.append(input_patronymic.get())
        value.append(input_address.get())
        phone_book[input_tel.get()] = value
        list_tel.insert(END, tel)
        label_info.config(text="Номер успешно добавлен")


def save():
    with open("Save", "w") as file:
        for tel in phone_book:
            value = phone_book[tel]
            temp = tel + ";" + value[0] + ";" + value[1] + ";" + value[2] + ";" + value[3] + "\n"
            file.write(temp)


def select_list_tel(evt):
    w = evt.widget
    i = int(w.curselection()[0])
    tel = w.get(i)
    

    value = phone_book[tel]
    last_name = value[0]
    first_name = value[1]
    patronymic_name = value[2]
    address_name = value[3]

    input_tel.insert(0, tel)
    input_last_name.insert(0, last_name)
    input_first_name.insert(0, first_name)
    input_patronymic.insert(0, patronymic)
    input_address.insert(0, address)

window = Tk()
window.title("PhoneBook")
window.geometry("550x250")

# Объявление элементов окна
label_tel = Label(text="Номер телефона")
input_tel = Entry()

label_last_name = Label(text="Фамилия")
input_last_name = Entry()
label_first_name = Label(text="Имя")
input_first_name = Entry()
label_patronymic = Label(text="Отчество")
input_patronymic = Entry()
label_address = Label(text="Адрес")
input_address = Entry()

label_tel.grid(row=0, column=0, padx=10, pady=5)
button_add = Button(text="Добавить", command=add)
button_clear = Button(text="Очистить", command=clear)
button_save = Button(text="Сохранить", command=save)

label_list_tel = Label(text="Список телефонов")
list_tel = Listbox()

label_info = Label(text="Программа готова к работе")

# Позиционирование
label_tel.grid(row=1, column=0, padx=10, pady=5, sticky="e")
input_tel.grid(row=1, column=1)

label_last_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
input_last_name.grid(row=2, column=1, padx=10)

label_first_name.grid(row=3, column=0, padx=10, pady=5, sticky="e")
input_first_name.grid(row=3, column=1)

label_patronymic.grid(row=4, column=0, padx=10, pady=5, sticky="e")
input_patronymic.grid(row=4, column=1, padx=10)

label_address.grid(row=5, column=0, padx=10, pady=5, sticky="e")
input_address.grid(row=5, column=1, pady=15)

button_add.grid(row=2, column=2, padx=20)
button_clear.grid(row=3, column=2, padx=20)
button_save.grid(row=4, column=2, padx=20)

label_list_tel.grid(row=2, column=3)
list_tel.grid(row=1, column=3, rowspan=4)

label_info.grid(row=0, column=1, columnspan=4, sticky="w")

list_tel.bind('<<ListboxSelect>>', select_list_tel)

window.mainloop()
