from tkinter import *
from tkinter.messagebox import showerror
import random
from tkinter import Toplevel, ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import time


class MainsWindows:
    def __init__(self, title, text, resizable, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap(default=icon)
        self.window.resizable(resizable, resizable)
        self.window.option_add("*tearOff", FALSE)
        if text != "":
            label = ttk.Label(self.window, text=text, justify="center", background="#FFCDD2", font="Arial,30",
                              padding=8)
            label.pack(expand=True)
        self.window.update()
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2 - self.window.winfo_width() // 2}+"
            f"{self.window.winfo_screenheight() // 2 - self.window.winfo_height() // 2}")


class AboutWindow:
    def __init__(self, mainwindow, title, text, image, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self._window = Toplevel(mainwindow)
        self._window.title(title)
        self._window["bg"] = "#FFCDD2"
        self._window.iconbitmap(default=icon)
        self._window.resizable(False, False)
        self._window.about = Image.open(image).resize((160, 180))
        self._window.about_tk = ImageTk.PhotoImage(self._window.about)
        ttk.Label(self._window, image=self._window.about_tk).pack(side='left')
        label = ttk.Label(self._window, text=text, justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label.pack(expand=True)
        self._window.update()
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_width() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_height() // 2}")
        self._window.grab_set()


class StartWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик",
                         "Курсовой проект\nСтедента: Гришко Д.И.\nПо теме:"
                         "\nСортировка числовых данных методом перемешивания",
                         FALSE)
        self.window.after(3000, self.close_start_window)
        self.main_window = None

    def close_start_window(self):
        self.window.destroy()
        self.main_window = MainWindow()
        self.main_window.window.mainloop()


class MainWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик",
                         "",
                         TRUE)
        self._data_entries = None
        self._result_label = None
        upper = "upper"
        downer = "downer"
        self.row = 0
        self.column = 0
        self.entries = []
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
                                    command=lambda: [
                                        GenerationWindow(self.window, 1000, self.frame, self.entries, self.canvas)])
        generation_menu.add_command(label="Генерировать случайные данные от 0 до 10000",
                                    command=lambda: [
                                        GenerationWindow(self.window, 10000, self.frame, self.entries, self.canvas)])
        generation_menu.add_command(label="Генерировать случайные данные от 0 до 100000",
                                    command=lambda: [
                                        GenerationWindow(self.window, 100000, self.frame, self.entries, self.canvas)])

        about.add_command(label="Об авторе", command=lambda: [AboutAuthor(self.window)])
        about.add_separator()
        about.add_command(label="О программе", command=lambda: [AboutProgram(self.window)])

        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Генерация чисел", menu=generation_menu)
        main_menu.add_cascade(label="Справка", menu=about)

        self.window.config(menu=main_menu)

        self.Sort = StringVar(value=upper)
        position = {"padx": 6, "pady": 6, "anchor": CENTER}
        self.btn_radio_up = ttk.Radiobutton(self.window, text="По возрастанию", value=upper, variable=self.Sort)
        self.btn_radio_up.pack(**position)
        self.btn_radio_down = ttk.Radiobutton(self.window, text="По убыванию", value=downer, variable=self.Sort)
        self.btn_radio_down.pack(**position)
        self.btn = ttk.Button(self.window, text="Сортировать",
                              command=lambda: self.sort(self.entries, self.Sort.get(), self.result_label))
        self.btn.pack(anchor="nw", padx=20, pady=6, fill=X)
        self.result_label = ttk.Label(self.window, text="")
        self.result_label.pack()
        self.btn1 = ttk.Button(self.window, text="Добавить элемент", command=self.add_entry)
        self.btn1.pack(anchor="nw", padx=20, pady=6, fill=X)
        self.btn2 = ttk.Button(self.window, text="Удалить элемент", command=self.delete_entry)
        self.btn2.pack(anchor="nw", padx=20, pady=6, fill=X)
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(side="top", fill="both",padx=20, pady=6, expand=True)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.HorScrollBar = tk.Scrollbar(self.window, orient="horizontal", command=self.canvas.xview)
        self.HorScrollBar.pack(side="bottom", fill="x")
        self.canvas.configure(xscrollcommand=self.HorScrollBar.set)
        self.canvas.bind('<Configure>', self.on_configure)
        self.window.update()
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2 - self.window.winfo_width() // 2}+"
            f"{self.window.winfo_screenheight() // 2 - self.window.winfo_height() // 2}")

    def add_entry(self):
        entry = tk.Entry(self.frame)
        self.entries.append(entry)
        self._rebuild_grid()

    def delete_entry(self):
        if self.entries:
            entry = self.entries.pop()
            entry.destroy()
            self._rebuild_grid()

    def _rebuild_grid(self):
        for i, entry in enumerate(self.entries):
            row = i % 10
            column = i // 10
            entry.grid(row=row, column=column, sticky="nsew")
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_configure(self, _):
        # Обновить область прокрутки при изменении размера холста
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def save_click(self):
        filepath = filedialog.asksaveasfilename(filetypes=[("Текстовые файлы", "*.txt")])
        if filepath != "":
            if not filepath.endswith(".txt"):
                filepath += ".txt"
            text = "\n".join(entry.get() for entry in self.entries)
            with open(filepath, "w") as file:
                file.write(text)

    def open_click(self):
        filepath = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
        if filepath != "":
            self.clean_click()
            with open(filepath, "r") as file:
                lines = file.readlines()

            # Удалить лишние поля ввода
            while len(self.entries) > len(lines):
                self.delete_entry()

            # Добавить недостающие поля ввода
            while len(self.entries) < len(lines):
                self.add_entry()

            # Вставить строки из файла в поля ввода
            for i, line in enumerate(lines):
                self.entries[i].delete(0, 'end')
                self.entries[i].insert(0, line.strip())
        self._rebuild_grid()

    def clean_click(self):
        for entry in self.entries:
            entry.destroy()
        self.entries = []
        self.result_label.config(text="")
        self._rebuild_grid()

    def exit_click(self):
        self.window.destroy()

    def sort(self, data_entries, type_sort, result_label):
        self._data_entries = data_entries
        self._result_label = result_label
        n = len(self._data_entries)
        try:

            for i in range(n):
                value = self._data_entries[i].get()
                if value == '':
                    raise ValueError(f"Значение в позиции {i} пустое")
                int(value)
            if n == 0:
                raise ValueError(f"Вы не добавили ни одного элемента")
        except ValueError as e:
            showerror("Ошибка", f"Ошибка: {e}")

        else:
            ArrayWindow(self._data_entries)
            start_time = time.time()
            if type_sort == "upper":
                swapped = True
                while swapped:
                    swapped = False
                    for i in range(n - 1):
                        a = int(self._data_entries[i].get())
                        b = int(self._data_entries[i + 1].get())
                        if a > b:
                            self._data_entries[i].delete(0, 'end')
                            self._data_entries[i].insert(0, str(b))
                            self._data_entries[i + 1].delete(0, 'end')
                            self._data_entries[i + 1].insert(0, str(a))
                            swapped = True
                    if not swapped:
                        break
                    swapped = False
                    for i in range(n - 1, 0, -1):
                        a = int(self._data_entries[i].get())
                        b = int(self._data_entries[i - 1].get())
                        if a < b:
                            self._data_entries[i].delete(0, 'end')
                            self._data_entries[i].insert(0, str(b))
                            self._data_entries[i - 1].delete(0, 'end')
                            self._data_entries[i - 1].insert(0, str(a))
                            swapped = True

            elif type_sort == "downer":
                swapped = True
                while swapped:
                    swapped = False
                    for i in range(n - 1):
                        a = int(self._data_entries[i].get())
                        b = int(self._data_entries[i + 1].get())
                        if a < b:
                            self._data_entries[i].delete(0, 'end')
                            self._data_entries[i].insert(0, str(b))
                            self._data_entries[i + 1].delete(0, 'end')
                            self._data_entries[i + 1].insert(0, str(a))
                            swapped = True
                    if not swapped:
                        break
                    swapped = False
                    for i in range(n - 1, 0, -1):
                        a = int(self._data_entries[i].get())
                        b = int(self._data_entries[i - 1].get())
                        if a > b:
                            self._data_entries[i].delete(0, 'end')
                            self._data_entries[i].insert(0, str(b))
                            self._data_entries[i - 1].delete(0, 'end')
                            self._data_entries[i - 1].insert(0, str(a))
                            swapped = True

            end_time = time.time()
            execution_time = round((end_time - start_time), 5)
            self._result_label.config(text=f"Время выполнения сортировки: {execution_time}")


class AboutAuthor(AboutWindow):
    def __init__(self, mainwindow):
        super().__init__(mainwindow, "Сведения об авторе",
                         "Автор: Гришко Дмитрий Игоревич\nГруппа: 10701222\nE-mail: dimagrishkoby@gmail.com ",
                         'materials/photo_2023-11-20_11-17-08.jpg')

class ArrayWindow:
    def __init__(self, data_entries):
        self._window = tk.Toplevel()
        self._window.title("Начальный массив")
        self.canvas = tk.Canvas(self._window)
        self.canvas.pack(side="top", fill="both", expand=True)

        self.entries = []
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.HorScrollBar = tk.Scrollbar(self._window, orient="horizontal", command=self.canvas.xview)
        self.HorScrollBar.pack(side="bottom", fill="x")
        self.canvas.configure(xscrollcommand=self.HorScrollBar.set)

        for i in range(len(data_entries)):
            entry = tk.Entry(self.frame)
            entry.insert(0, data_entries[i].get())
            entry.grid()  # Здесь используется pack
            self.entries.append(entry)
        self._rebuild_grid()

    def _rebuild_grid(self):
        for i, entry in enumerate(self.entries):
            row = i % 10
            column = i // 10
            entry.grid(row=row, column=column, sticky="nsew")  # Здесь используется grid
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class AboutProgram(AboutWindow):
    def __init__(self, mainwindow):
        super().__init__(mainwindow, "О программе: Сортировщик",
                         "Программа сортирует числовые данные\nПри помощи метода перемешивания"
                         "\nЭта программа использует алгоритм сортировки перемешиванием\n "
                         "(или коктейльной сортировки), который является вариацией пузырьковой сортировки.\n "
                         "Он проходит через список элементов в обоих направлениях, сначала слева направо,\n"
                         " а затем справа налево, сравнивая пары соседних элементов и меняя их местами,\n "
                         "если они расположены в неправильном порядке. Это продолжается до тех пор,\n "
                         "пока не будет выполнен проход, в котором не требуется никаких обменов, "
                         "что указывает на то,\n что список отсортирован. Этот алгоритм"
                         " эффективен для списков, которые уже частично отсортированы.",
                         'materials/images.png')


class GenerationWindow:
    def __init__(self, mainwindow, digit, frame, entries, canvas, icon=""):
        self._window = Toplevel(mainwindow)
        self._window.title("Генератор чисел")
        self._window.iconbitmap(default=icon)
        self._window.resizable(True, True)
        self._frame = frame
        self._entries = entries
        self._canvas = canvas
        label1 = ttk.Label(self._window,
                           text="Введите количество гинерируемых чисел: ",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label1.pack(expand=True)
        digit_count_entry = Entry(self._window)
        digit_count_entry.pack(padx=5, pady=5)

        btn1 = ttk.Button(self._window, text="Генерировать",
                          command=lambda: self._generate_numbers(self._window, digit, digit_count_entry))
        btn1.pack(anchor="nw", padx=20, pady=30, fill=X)
        self._window.update()
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_width() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_height() // 2}")
        self._window.grab_set()

    def _generate_numbers(self, window, digit, digit_count_entry):
        try:
            digit_count = int(digit_count_entry.get())
        except ValueError:
            showerror(title="Ошибка", message="Введено недопустимое значение. Пожалуйста, введите число.")
        else:
            self._generation(digit, digit_count)
            window.destroy()

    def _generation(self, digit, digit_count):
        for i in range(digit_count):  # Пример: 33 элемента
            random_digit = random.randint(0, digit)
            entry = tk.Entry(self._frame)
            entry.insert(0, f"{random_digit}")
            entry.grid(row=i % 10, column=i // 10, sticky="nsew")
            self._entries.append(entry)
        self._frame.update_idletasks()
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))


start_window = StartWindow()
start_window.window.mainloop()
