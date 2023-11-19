from tkinter import *
from tkinter import ttk
from tkinter import Tk
import random

def create_main_window():
    mainwindow = Tk()
    mainwindow.title("Программа сортировщик")
    mainwindow.iconbitmap(default="materials/sort-2_icon-icons.com_69583.ico")
    mainwindow.geometry("500x500+%d+%d" % (x, y))  # устанавливаем размеры окна
    mainwindow.option_add("*tearOff", FALSE)

    def sort(type_sort):
        if type_sort == "upper":
            n = digit_data_listbox.size()
            swapped = True
            start = 0
            end = n - 1

            while swapped:
                swapped = False

                # проходим слева направо
                for i in range(start, end):
                    if int(digit_data_listbox.get(i)) > int(digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = digit_data_listbox.get(i)
                        digit_data_listbox.delete(i)
                        digit_data_listbox.insert(i, digit_data_listbox.get(i))
                        digit_data_listbox.delete(i + 1)
                        digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # если не было обмена, список отсортирован
                if not swapped:
                    break

                swapped = False

                # уменьшаем конец на один, так как последний элемент уже на своем месте
                end -= 1

                # проходим справа налево
                for i in range(end - 1, start - 1, -1):
                    if int(digit_data_listbox.get(i)) > int(digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = digit_data_listbox.get(i)
                        digit_data_listbox.delete(i)
                        digit_data_listbox.insert(i, digit_data_listbox.get(i))
                        digit_data_listbox.delete(i + 1)
                        digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # увеличиваем начало, так как следующий первый элемент уже отсортирован
                start += 1
        if type_sort == "downer":
            n = digit_data_listbox.size()
            swapped = True
            start = 0
            end = n - 1

            while swapped:
                swapped = False

                # проходим слева направо
                for i in range(start, end):
                    if int(digit_data_listbox.get(i)) < int(digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = digit_data_listbox.get(i)
                        digit_data_listbox.delete(i)
                        digit_data_listbox.insert(i, digit_data_listbox.get(i))
                        digit_data_listbox.delete(i + 1)
                        digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # если не было обмена, список отсортирован
                if not swapped:
                    break

                swapped = False

                # уменьшаем конец на один, так как последний элемент уже на своем месте
                end -= 1

                # проходим справа налево
                for i in range(end - 1, start - 1, -1):
                    if int(digit_data_listbox.get(i)) < int(digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = digit_data_listbox.get(i)
                        digit_data_listbox.delete(i)
                        digit_data_listbox.insert(i, digit_data_listbox.get(i))
                        digit_data_listbox.delete(i + 1)
                        digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # увеличиваем начало, так как следующий первый элемент уже отсортирован
                start += 1

    def sort_type():
        sort_type_window = Tk()
        sort_type_window.title("Выбор режима сортировки")
        sort_type_window.iconbitmap(default="materials/sort-2_icon-icons.com_69583.ico")
        sort_type_window.geometry("+%d+%d" % (x, y))  # устанавливаем размеры окна
        sort_type_window.option_add("*tearOff", FALSE)
        label1 = ttk.Label(sort_type_window,
                           text="Выберите тип сортировки: ",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label1.pack(expand=True)
        btn1 = ttk.Button(sort_type_window, text="По возрастанию",
                          command=lambda: [sort("upper"), sort_type_window.destroy()])
        btn1.pack(anchor="nw", padx=20, pady=30, fill=X)
        btn2 = ttk.Button(sort_type_window, text="По убыванию",
                          command=lambda: [sort("downer"), sort_type_window.destroy()])
        btn2.pack(anchor="nw", padx=20, pady=30, fill=X)

    def save_click():
        pass

    def save_how_click():
        pass

    def open_click():
        pass

    def clean_click():
        digit_data_listbox.delete(0, 'end')

    def exit_click():
        mainwindow.destroy()

    def change_item(event):
        # получаем индекс выделенного элемента
        index = digit_data_listbox.curselection()[0]
        # получаем новый текст из поля ввода
        new_digit = digit_data_entry.get()
        # заменяем элемент по индексу на новый текст
        digit_data_listbox.delete(index)
        digit_data_listbox.insert(index, new_digit)

    def generation(digit, digit_count):
        for _ in range(digit_count):
            random_digit = random.randint(0, digit)
            digit_data_listbox.insert(0, random_digit)

    def digit_generation(digit):
        digitgeneration = Toplevel(mainwindow)
        digitgeneration.title("Генератор чисел")
        digitgeneration.iconbitmap(default="materials/sort-2_icon-icons.com_69583.ico")
        digitgeneration.geometry("+%d+%d" % (x, y))
        digitgeneration.resizable(False, False)
        label1 = ttk.Label(digitgeneration,
                           text="Введите количество гинерируемых чисел: ",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label1.pack(expand=True)

        digit_count_entry = Entry(digitgeneration)
        digit_count_entry.pack(padx=5, pady=5)

        btn1 = ttk.Button(digitgeneration, text="Генерировать",
                          command=lambda: [generation(digit, int(digit_count_entry.get()))])
        btn1.pack(anchor="nw", padx=20, pady=30, fill=X)
        digitgeneration.grab_set()

    def about_author():
        aboutauthor_window = Toplevel(mainwindow)
        aboutauthor_window.title("Сведения об авторе")
        aboutauthor_window.iconbitmap(default="materials/sort-2_icon-icons.com_69583.ico")
        aboutauthor_window.geometry("+%d+%d" % (x, y))
        aboutauthor_window.resizable(False, False)
        label1 = ttk.Label(aboutauthor_window,
                           text="Автор: Гришко Дмитрий Игоревич\nГруппа: 10701222\nE-mail: dimagrishkoby@gmail.com",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label1.pack(expand=True)
        aboutauthor_window.grab_set()

    def about_programm():
        aboutprogramm_window = Toplevel(mainwindow)
        aboutprogramm_window.title("О программе: Сортировщик")
        aboutprogramm_window.geometry("+%d+%d" % (x, y))
        aboutprogramm_window.resizable(False, False)

        label1 = ttk.Label(aboutprogramm_window,
                           text="Программа сортирует числовые данные\nПри помощи метода перемешивания",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label1.pack(expand=True)
        aboutprogramm_window.grab_set()

    main_menu = Menu()
    file_menu = Menu()
    about = Menu()
    generation_menu = Menu()
    file_menu.add_command(label="Сохранить", command=save_click)
    file_menu.add_command(label="Сохранить как", command=save_how_click)
    file_menu.add_command(label="Открыть", command=open_click)
    file_menu.add_command(label="Очистить", command=clean_click)
    file_menu.add_separator()
    file_menu.add_command(label="Выход", command=exit_click)

    generation_menu.add_command(label="Генерировать случайные данные от 0 до 1000",
                                command=lambda: [digit_generation(1000)])
    generation_menu.add_command(label="Генерировать случайные данные от 0 до 10000",
                                command=lambda: [digit_generation(10000)])
    generation_menu.add_command(label="Генерировать случайные данные от 0 до 100000",
                                command=lambda: [digit_generation(100000)])

    about.add_command(label="Об авторе", command=about_author)
    about.add_separator()
    about.add_command(label="О программе", command=about_programm)

    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_cascade(label="Генерация чисел", menu=generation_menu)
    main_menu.add_cascade(label="Справка", menu=about)

    mainwindow.config(menu=main_menu)
    # mainwindow.resizable(False, False)
    btn = ttk.Button(text="Сортировать", command=sort_type)
    btn.pack(anchor="nw", padx=20, pady=30, fill=X)

    # btn1 = ttk.Button(text = "")

    digit_data = []
    digit_data_var = Variable(value=digit_data)

    digit_data_listbox = Listbox(listvariable=digit_data_var)

    digit_data_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
    # привязываем событие двойного щелчка к listbox
    digit_data_listbox.bind("<Double-Button-1>", change_item)

    # создаем поле ввода для нового текста
    digit_data_entry = Entry()
    digit_data_entry.pack(padx=5, pady=5)
    mainwindow.mainloop()


def close_start_window():
    startwindow.destroy()
    create_main_window()


startwindow = Tk()  # создаем корневой объект - окно
startwindow.title("Программа сортировщик")  # устанавливаем заголовок окна
startwindow.iconbitmap(default="materials/sort-2_icon-icons.com_69583.ico")
x = (startwindow.winfo_screenwidth() - startwindow.winfo_reqwidth()) / 2
y = (startwindow.winfo_screenheight() - startwindow.winfo_reqheight()) / 2
startwindow.geometry("+%d+%d" % (x, y))  # устанавливаем размеры окна
startwindow.resizable(False, False)
label = ttk.Label(
    text="Курсовой проект\nСтедента: Гришко Д.И.\nПо теме:\nСортировка числовых данных методом перемешивания",
    justify="center", background="#FFCDD2", font="Arial,30", padding=8)
label.pack(expand=True)
startwindow.after(3000, close_start_window)  # Закрыть стартовое окно через 3 секунды
startwindow.mainloop()
