from tkinter import *
from tkinter.messagebox import showerror
import random
from tkinter import Toplevel, ttk
import time


class MainsWindows:
    def __init__(self, title, text, resizable, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap(default=icon)
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
        self.window.geometry("+%d+%d" % (x, y))
        self.window.resizable(resizable, resizable)
        self.window.option_add("*tearOff", FALSE)
        if text != "":
            label = ttk.Label(self.window, text=text, justify="center", background="#FFCDD2", font="Arial,30",
                              padding=8)
            label.pack(expand=True)


class MainWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик",
                         "",
                         TRUE)
        self.window.geometry("500x300")  # устанавливаем размеры окна

        def sort(type_sort):

            if type_sort == "upper":
                n = self.digit_data_listbox.size()
                swapped = True
                start = 0
                end = n - 1

                while swapped:
                    swapped = False

                    # проходим слева направо
                    for i in range(start, end):
                        if int(self.digit_data_listbox.get(i)) > int(
                                self.digit_data_listbox.get(i + 1)):
                            # меняем местами
                            temp = self.digit_data_listbox.get(i)
                            self.digit_data_listbox.delete(i)
                            self.digit_data_listbox.insert(i, self.digit_data_listbox.get(i))
                            self.digit_data_listbox.delete(i + 1)
                            self.digit_data_listbox.insert(i + 1, temp)

                            swapped = True

                    # если не было обмена, список отсортирован
                    if not swapped:
                        break

                    swapped = False

                    # уменьшаем конец на один, так как последний элемент уже на своем месте
                    end -= 1

                    # проходим справа налево
                    for i in range(end - 1, start - 1, -1):
                        if int(self.digit_data_listbox.get(i)) > int(
                                self.digit_data_listbox.get(i + 1)):
                            # меняем местами
                            temp = self.digit_data_listbox.get(i)
                            self.digit_data_listbox.delete(i)
                            self.digit_data_listbox.insert(i, self.digit_data_listbox.get(i))
                            self.digit_data_listbox.delete(i + 1)
                            self.digit_data_listbox.insert(i + 1, temp)

                            swapped = True

                    # увеличиваем начало, так как следующий первый элемент уже отсортирован
                    start += 1
            if type_sort == "downer":
                n = self.digit_data_listbox.size()
                swapped = True
                start = 0
                end = n - 1

                while swapped:
                    swapped = False

                    # проходим слева направо
                    for i in range(start, end):
                        if int(self.digit_data_listbox.get(i)) < int(
                                self.digit_data_listbox.get(i + 1)):
                            # меняем местами
                            temp = self.digit_data_listbox.get(i)
                            self.digit_data_listbox.delete(i)
                            self.digit_data_listbox.insert(i, self.digit_data_listbox.get(i))
                            self.digit_data_listbox.delete(i + 1)
                            self.digit_data_listbox.insert(i + 1, temp)

                            swapped = True

                    # если не было обмена, список отсортирован
                    if not swapped:
                        break

                    swapped = False

                    # уменьшаем конец на один, так как последний элемент уже на своем месте
                    end -= 1

                    # проходим справа налево
                    for i in range(end - 1, start - 1, -1):
                        if int(self.digit_data_listbox.get(i)) < int(self.digit_data_listbox.get(i + 1)):
                            # меняем местами
                            temp = self.digit_data_listbox.get(i)
                            self.digit_data_listbox.delete(i)
                            self.digit_data_listbox.insert(i, self.digit_data_listbox.get(i))
                            self.digit_data_listbox.delete(i + 1)
                            self.digit_data_listbox.insert(i + 1, temp)

                            swapped = True

                    # увеличиваем начало, так как следующий первый элемент уже отсортирован
                    start += 1

        def sort_type():
            sort_type_window = Tk()
            sort_type_window.title("Выбор режима сортировки")
            sort_type_window.iconbitmap(default="materials/sort-2_icon-icons.com_69583.ico")
            x = (sort_type_window.winfo_screenwidth() - sort_type_window.winfo_reqwidth()) / 2
            y = (sort_type_window.winfo_screenheight() - sort_type_window.winfo_reqheight()) / 2
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

        def open_click():
            pass

        def clean_click():
            self.digit_data_listbox.delete(0, 'end')

        def exit_click():
            self.window.destroy()

        def change_item(event):
            # получаем индекс выделенного элемента
            index = self.digit_data_listbox.curselection()[0]
            # получаем новый текст из поля ввода
            new_digit = self.digit_data_entry.get()
            # заменяем элемент по индексу на новый текст
            self.digit_data_listbox.delete(index)
            self.digit_data_listbox.insert(index, new_digit)

        def generation(digit, digit_count):
            for _ in range(digit_count):
                random_digit = random.randint(0, digit)
                self.digit_data_listbox.insert(0, random_digit)

        def digit_generation(digit):
            digitgeneration = Toplevel(self.window)
            digitgeneration.title("Генератор чисел")
            digitgeneration.iconbitmap(default="materials/sort-2_icon-icons.com_69583.ico")
            digitgeneration.resizable(False, False)
            label1 = ttk.Label(digitgeneration,
                               text="Введите количество гинерируемых чисел: ",
                               justify="center", background="#FFCDD2", font="Arial,30", padding=8)
            label1.pack(expand=True)
            digit_count_entry = Entry(digitgeneration)
            digit_count_entry.pack(padx=5, pady=5)

            btn1 = ttk.Button(digitgeneration, text="Генерировать",
                              command=lambda: generate_numbers(digit, digit_count_entry, digitgeneration))
            btn1.pack(anchor="nw", padx=20, pady=30, fill=X)
            digitgeneration.grab_set()

        def generate_numbers(digit, digit_count_entry, digitgeneration):
            try:
                digit_count = int(digit_count_entry.get())
            except ValueError:
                showerror(title="Ошибка", message="Введено недопустимое значение. Пожалуйста, введите число.")
            else:
                generation(digit, digit_count)
                digitgeneration.destroy()

        main_menu = Menu()
        file_menu = Menu()
        about = Menu()
        generation_menu = Menu()
        file_menu.add_command(label="Сохранить", command=save_click)
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

        about.add_command(label="Об авторе", command=lambda: [AboutAuthor(self.window)])
        about.add_separator()
        about.add_command(label="О программе", command=lambda: [AboutProgram(self.window)])

        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Генерация чисел", menu=generation_menu)
        main_menu.add_cascade(label="Справка", menu=about)

        self.window.config(menu=main_menu)
        self.btn = ttk.Button(self.window, text="Сортировать", command=sort_type)
        self.btn.pack(anchor="nw", padx=20, pady=30, fill=X)
        self.digit_data = []
        self.digit_data_var = Variable(value=self.digit_data)
        self.digit_data_listbox = Listbox(listvariable=self.digit_data_var)
        self.digit_data_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

        # привязываем событие двойного щелчка к listbox
        self.digit_data_listbox.bind("<Double-Button-1>", change_item)

        # создаем поле ввода для нового текста
        self.digit_data_entry = Entry()
        self.digit_data_entry.pack(padx=5, pady=5)
        # self.mainwindow.mainloop()


class AboutWindow:
    def __init__(self, mainwindow, title, text, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self.window = Toplevel(mainwindow)
        self.window.title(title)
        self.window.iconbitmap(default=icon)
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
        self.window.geometry("+%d+%d" % (x, y))
        self.window.resizable(False, False)
        label = ttk.Label(self.window, text=text, justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label.pack(expand=True)
        self.window.grab_set()


class AboutAuthor(AboutWindow):
    def __init__(self, mainwindow):
        super().__init__(mainwindow, "Сведения об авторе",
                         "Автор: Гришко Дмитрий Игоревич\nГруппа: 10701222\nE-mail: dimagrishkoby@gmail.com")


class AboutProgram(AboutWindow):
    def __init__(self, mainwindow):
        super().__init__(mainwindow, "О программе: Сортировщик",
                         "Программа сортирует числовые данные\nПри помощи метода перемешивания")


class StartWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик",
                         "Курсовой проект\nСтедента: Гришко Д.И.\nПо теме:\nСортировка числовых данных методом перемешивания",
                         FALSE)
        self.window.after(3000, self.close_start_window)

    def close_start_window(self):
        self.window.destroy()
        self.main_window = MainWindow()
        self.main_window.window.mainloop()


start_window = StartWindow()
start_window.window.mainloop()
