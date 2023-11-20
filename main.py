from tkinter import *
from tkinter.messagebox import showerror
import random
from tkinter import Toplevel, ttk
from PIL import Image, ImageTk
import time


class MainsWindows:
    def __init__(self, title, text, resizable, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap(default=icon)
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2 - self.window.winfo_reqwidth() // 2}+"
            f"{self.window.winfo_screenheight() // 2 - self.window.winfo_reqwidth() // 2}")
        self.window.resizable(resizable, resizable)
        self.window.option_add("*tearOff", FALSE)
        if text != "":
            label = ttk.Label(self.window, text=text, justify="center", background="#FFCDD2", font="Arial,30",
                              padding=8)
            label.pack(expand=True)


class AboutWindow:
    def __init__(self, mainwindow, title, text, image, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self._window = Toplevel(mainwindow)
        self._window.title(title)
        self._window["bg"] = "#FFCDD2"
        self._window.iconbitmap(default=icon)
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_reqwidth() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_reqwidth() // 2}")
        self._window.resizable(False, False)
        self._window.about = Image.open(image).resize((160, 180))
        self._window.about_tk = ImageTk.PhotoImage(self._window.about)
        ttk.Label(self._window, image=self._window.about_tk).pack(side='left')
        label = ttk.Label(self._window, text=text, justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label.pack(expand=True)
        self._window.grab_set()


class StartWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик",
                         "Курсовой проект\nСтедента: Гришко Д.И.\nПо теме:"
                         "\nСортировка числовых данных методом перемешивания",
                         FALSE)
        self.window.after(3000, self.close_start_window)

    def close_start_window(self):
        self.window.destroy()
        self.main_window = MainWindow()
        self.main_window.window.mainloop()


class MainWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик",
                         "",
                         TRUE)
        self.window.geometry("550x350")  # устанавливаем размеры окна

        main_menu = Menu()
        file_menu = Menu()
        about = Menu()
        generation_menu = Menu()
        file_menu.add_command(label="Сохранить", command=self.save_click)
        file_menu.add_command(label="Открыть", command=self.open_click)
        file_menu.add_command(label="Очистить", command=self.clean_click)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_click)

        generation_menu.add_command(label="Генерировать случайные данные от 0 до 1000",
                                    command=lambda: [GenerationWindow(self.window, 1000, self.digit_data_listbox)])
        generation_menu.add_command(label="Генерировать случайные данные от 0 до 10000",
                                    command=lambda: [GenerationWindow(self.window, 10000, self.digit_data_listbox)])
        generation_menu.add_command(label="Генерировать случайные данные от 0 до 100000",
                                    command=lambda: [GenerationWindow(self.window, 100000, self.digit_data_listbox)])

        about.add_command(label="Об авторе", command=lambda: [AboutAuthor(self.window)])
        about.add_separator()
        about.add_command(label="О программе", command=lambda: [AboutProgram(self.window)])

        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Генерация чисел", menu=generation_menu)
        main_menu.add_cascade(label="Справка", menu=about)

        self.window.config(menu=main_menu)
        upper = "upper"
        downer = "downer"
        self.sort = StringVar(value=upper)
        position = {"padx": 6, "pady": 6, "anchor": CENTER}
        self.btn_radio_up = ttk.Radiobutton(self.window, text="По вохрастанию", value=upper, variable=self.sort)
        self.btn_radio_up.pack(**position)
        self.btn_radio_down = ttk.Radiobutton(self.window, text="По убыванию", value=downer, variable=self.sort)
        self.btn_radio_down.pack(**position)

        self.btn = ttk.Button(self.window, text="Сортировать",
                              command=lambda: [Sorted.sort(self.window, self.digit_data_listbox, self.sort.get(),
                                                           self.result_label)])
        self.btn.pack(anchor="nw", padx=20, pady=6, fill=X)
        self.result_label = ttk.Label(self.window, text="")
        self.result_label.pack()
        self.digit_data = []
        self.digit_data_var = Variable(value=self.digit_data)
        self.digit_data_listbox = Listbox(listvariable=self.digit_data_var)
        self.digit_data_listbox.pack(expand=True, fill=BOTH, padx=5, pady=5)

        # привязываем событие двойного щелчка к listbox
        self.digit_data_listbox.bind("<Double-Button-1>", self.change_item)

        # создаем поле ввода для нового текста
        self.label2 = ttk.Label(self.window,
                                text="Введите значение на которое нужно поменять, "
                                     "после чего дважды кликните на нужный элемент:")
        self.label2.pack(expand=True)
        self.digit_data_entry = Entry()
        self.digit_data_entry.pack(expand=True, padx=5, pady=5)

    def save_click(self):

        pass

    def open_click(self):
        pass

    def clean_click(self):
        self.digit_data_listbox.delete(0, 'end')

    def exit_click(self):
        self.window.destroy()

    def change_item(self, event):
        try:
            # получаем индекс выделенного элемента
            index = self.digit_data_listbox.curselection()[0]
            # получаем новый текст из поля ввода

        except IndexError:
            showerror("Ошибка", "Вы промахнулись, попробуйте снова!")

        else:
            try:
                new_digit = int(self.digit_data_entry.get())
            except ValueError:
                showerror("Ошибка", "Вы ввели не верное значение")
            else:
                # заменяем элемент по индексу на новый текст
                self.digit_data_listbox.delete(index)
                self.digit_data_listbox.insert(index, new_digit)


class Sorted:

    def __init__(self):
        self._digit_data_listbox = None
        self._result_label = None

    def sort(self, digit_data_listbox, type_sort, result_label):
        self._digit_data_listbox = digit_data_listbox
        self._result_label = result_label
        if type_sort == "upper":
            n = self._digit_data_listbox.size()
            swapped = True
            start = 0
            end = n - 1
            start_time = time.time()
            while swapped:
                swapped = False

                # проходим слева направо
                for i in range(start, end):
                    if int(self._digit_data_listbox.get(i)) > int(
                            self._digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = self._digit_data_listbox.get(i)
                        self._digit_data_listbox.delete(i)
                        self._digit_data_listbox.insert(i, self._digit_data_listbox.get(i))
                        self._digit_data_listbox.delete(i + 1)
                        self._digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # если не было обмена, список отсортирован
                if not swapped:
                    break

                swapped = False

                # уменьшаем конец на один, так как последний элемент уже на своем месте
                end -= 1

                # проходим справа налево
                for i in range(end - 1, start - 1, -1):
                    if int(self._digit_data_listbox.get(i)) > int(
                            self._digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = self._digit_data_listbox.get(i)
                        self._digit_data_listbox.delete(i)
                        self._digit_data_listbox.insert(i, self._digit_data_listbox.get(i))
                        self._digit_data_listbox.delete(i + 1)
                        self._digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # увеличиваем начало, так как следующий первый элемент уже отсортирован
                start += 1
            end_time = time.time()

        if type_sort == "downer":
            n = self._digit_data_listbox.size()
            swapped = True
            start = 0
            end = n - 1
            start_time = time.time()

            while swapped:
                swapped = False

                # проходим слева направо
                for i in range(start, end):
                    if int(self._digit_data_listbox.get(i)) < int(
                            self._digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = self._digit_data_listbox.get(i)
                        self._digit_data_listbox.delete(i)
                        self._digit_data_listbox.insert(i, self._digit_data_listbox.get(i))
                        self._digit_data_listbox.delete(i + 1)
                        self._digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # если не было обмена, список отсортирован
                if not swapped:
                    break

                swapped = False

                # уменьшаем конец на один, так как последний элемент уже на своем месте
                end -= 1

                # проходим справа налево
                for i in range(end - 1, start - 1, -1):
                    if int(self._digit_data_listbox.get(i)) < int(self._digit_data_listbox.get(i + 1)):
                        # меняем местами
                        temp = self._digit_data_listbox.get(i)
                        self._digit_data_listbox.delete(i)
                        self._digit_data_listbox.insert(i, self._digit_data_listbox.get(i))
                        self._digit_data_listbox.delete(i + 1)
                        self._digit_data_listbox.insert(i + 1, temp)

                        swapped = True

                # увеличиваем начало, так как следующий первый элемент уже отсортирован
                start += 1
                end_time = time.time()
        execution_time = round((end_time - start_time), 5)
        self._result_label.config(text=f"Время выполнения сортировки: {execution_time}")


class AboutAuthor(AboutWindow):
    def __init__(self, mainwindow):
        super().__init__(mainwindow, "Сведения об авторе",
                         "Автор: Гришко Дмитрий Игоревич\nГруппа: 10701222\nE-mail: dimagrishkoby@gmail.com",
                         'materials/photo_2023-11-20_11-17-08.jpg')


class AboutProgram(AboutWindow):
    def __init__(self, mainwindow):
        super().__init__(mainwindow, "О программе: Сортировщик",
                         "Программа сортирует числовые данные\nПри помощи метода перемешивания", 'materials/images.png')


class GenerationWindow:
    def __init__(self, mainwindow, digit, digit_data_listbox, icon=""):
        self._window = Toplevel(mainwindow)
        self._window.title("Генератор чисел")
        self._window.iconbitmap(default=icon)
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_reqwidth() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_reqwidth() // 2}")
        self._window.resizable(True, True)
        self._digit_data_listbox = digit_data_listbox
        label1 = ttk.Label(self._window,
                           text="Введите количество гинерируемых чисел: ",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label1.pack(expand=True)
        digit_count_entry = Entry(self._window)
        digit_count_entry.pack(padx=5, pady=5)

        btn1 = ttk.Button(self._window, text="Генерировать",
                          command=lambda: self._generate_numbers(digit, digit_count_entry, self._window))
        btn1.pack(anchor="nw", padx=20, pady=30, fill=X)
        self._window.grab_set()

    def _generate_numbers(self, digit, digit_count_entry, digitgeneration):
        try:
            digit_count = int(digit_count_entry.get())
        except ValueError:
            showerror(title="Ошибка", message="Введено недопустимое значение. Пожалуйста, введите число.")
        else:
            self._generation(digit, digit_count)
            digitgeneration.destroy()

    def _generation(self, digit, digit_count):
        for _ in range(digit_count):
            random_digit = random.randint(0, digit)
            self._digit_data_listbox.insert(0, random_digit)


start_window = StartWindow()
start_window.window.mainloop()
