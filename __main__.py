from tkinter import *
from tkinter.messagebox import showerror, askyesnocancel

from tkinter import ttk
import tkinter as tk

from tkinter import filedialog
import time
import os
from modules.about_windows import AboutAuthor, AboutProgram
from modules.generate_window import GenerationWindow
from modules.main_windows import MainsWindows
from modules.array_window import ArrayWindow


class MainWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик",
                         "", "", "", "", "", "", "", "",
                         TRUE, None)
        self._data_entries = None
        self._result_label = None
        upper = "upper"
        downer = "downer"
        position = {"padx": 6, "pady": 6, "anchor": CENTER}
        self.row = 0
        self.column = 0
        self.entries = []
        self.current_file = None
        self.current_directory = os.getcwd()
        main_menu = Menu()
        file_menu = Menu()
        about = Menu()

        file_menu.add_command(label="Сохранить", command=self.save_click)
        file_menu.add_command(label="Сохранить как", command=self.save_how_click)
        file_menu.add_command(label="Открыть", command=self.open_click)
        file_menu.add_command(label="Очистить", command=self.clean_click)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_click)

        about.add_command(label="Об авторе", command=lambda: [AboutAuthor(self.window)])
        about.add_separator()
        about.add_command(label="О программе", command=lambda: [AboutProgram(self.window)])

        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Справка", menu=about)

        self.window.config(menu=main_menu)
        self.btn_generation = ttk.Button(self.window, text="Генерировать числа",
                                         command=lambda: [self.generation()])
        self.btn_generation.pack(anchor="nw", padx=20, pady=6, fill=X)
        self.Sort = StringVar(value=upper)

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
        self.canvas = tk.Canvas(self.window, height=240)
        self.canvas.pack(side="top", fill="both", padx=20, pady=6, expand=True)

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

    def generation(self):
        def on_generation():
            self.rebuild_grid()

        GenerationWindow(self.window, self.frame, self.entries, self.canvas, on_generation)

    def add_entry(self):
        entry = tk.Entry(self.frame, width=10)  # Set a fixed width for the empty entry
        self.entries.append(entry)
        self.rebuild_grid()

    def delete_entry(self):
        if self.entries:
            entry = self.entries.pop()
            entry.grid_forget()  # Forget the grid position
            entry.destroy()  # Destroy the entry widget
            self.rebuild_grid()

    def rebuild_grid(self):

        for widget in self.frame.winfo_children():
            widget.grid_forget()

        max_widths = [0] * 10

        for i, entry in enumerate(self.entries):
            row = i % 10
            column = i // 10
            entry.grid(row=row, column=column, sticky="nsew")

            # Use a hidden label for accurate measurement of entry width
            hidden_label = tk.Label(self.frame, text=entry.get(), font=entry['font'])
            text_width = hidden_label.winfo_width() + 5  # Add 5 pixels to the width
            hidden_label.destroy()  # Destroy the hidden label after measurement

            if column < 10:
                max_widths[column] = max(max_widths[column], text_width)

        for i, width in enumerate(max_widths):
            self.frame.columnconfigure(i, minsize=width)

        for i, entry in enumerate(self.entries):
            column = i % 10
            # Set the width of empty entries to the width of the longest entry in the column
            entry_width = max_widths[column] if entry.get() else 0
            entry.config(width=entry_width, justify='left')

        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_configure(self, _):
        # Обновить область прокрутки при изменении размера холста
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def save_click(self):

        if self.current_file is None:
            self.current_file = filedialog.asksaveasfilename(initialdir=self.current_directory,
                                                             filetypes=[("Текстовые файлы", "*.txt")])
            if not self.current_file:  # Если пользователь нажал "Отмена", self.current_file будет пустой строкой
                return  # Прервать выполнение функции
            if not self.current_file.endswith(".txt"):
                self.current_file += ".txt"

        if self.current_file != "":
            text = "\n".join(entry.get() for entry in self.entries)
            with open(self.current_file, "w") as file:
                file.write(text)

    def save_how_click(self):

        self.current_file = filedialog.asksaveasfilename(initialdir=self.current_directory,
                                                         filetypes=[("Текстовые файлы", "*.txt")])
        if self.current_file != "":
            if not self.current_file.endswith(".txt"):
                self.current_file += ".txt"
            text = "\n".join(entry.get() for entry in self.entries)
            with open(self.current_file, "w") as file:
                file.write(text)

    def open_click(self):
        self.clean_click()
        self.current_file = filedialog.askopenfilename(initialdir=self.current_directory,
                                                       filetypes=[("Текстовые файлы", "*.txt")])
        if self.current_file:  # Если пользователь нажал "Отмена", self.current_file будет None

            if self.current_file is not None:
                with open(self.current_file, "r") as file:
                    lines = file.readlines()

                # Отключить обновление интерфейса
                self.window.update_idletasks()
                self.window.after_idle(self.window.update_idletasks)

                # Удалить лишние поля ввода
                while len(self.entries) > len(lines):
                    self.entries[-1].grid_forget()
                    self.entries.pop()

                # Добавить недостающие поля ввода
                while len(self.entries) < len(lines):
                    entry = tk.Entry(self.frame)
                    entry.grid()
                    self.entries.append(entry)

                # Вставить строки из файла в поля ввода
                for i, line in enumerate(lines):
                    self.entries[i].delete(0, 'end')
                    self.entries[i].insert(0, line.strip())

                # Включить обновление интерфейса
                self.window.after_idle(self.window.update_idletasks)
                self.rebuild_grid()

    def clean_click(self):
        if self.current_file is None:
            if self.entries:
                result = askyesnocancel(title="Вы не сохранили файл", message="Вы хотите сохранить этот файл?")
                if result:
                    self.save_click()
                elif result is None:  # Если пользователь нажал "Отмена"
                    return  # Прервать выполнение функции
                else:  # Если пользователь нажал "Нет"
                    for entry in self.entries:
                        entry.destroy()
                    self.entries = []
                    self.result_label.config(text="")
            else:
                for entry in self.entries:
                    entry.destroy()
                self.entries = []
                self.result_label.config(text="")
        else:
            for entry in self.entries:
                entry.destroy()
            self.entries = []
            self.result_label.config(text="")
            self.current_file = None
            self.rebuild_grid()

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
            ArrayWindow(self.window, self._data_entries)
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


class StartWindow(MainsWindows):
    def __init__(self):
        super().__init__("Программа сортировщик", "Белорусский Национальный"
                                                  " технический университет",
                         "Факультет информационных технологий и"
                         " робототехники\n Кафедра программного"
                         " обеспечиния информационных систем и технологий ",
                         "Курсовая работа",
                         "по дисциплине языки программирования",
                         "Сортировка числовых данных методом перемешивания",
                         "Выполнил: Cтудент группы 10701222\nГришко Дмитрий Игоревич\n\n\nПреподаватель:к.ф-м.н.,доц."
                         "\nСидорик Валерий Владимирович",
                         'materials/OIG.4r2eWaC.png',
                         "Минск, 2023",
                         FALSE, MainWindow)
        self.btn1 = ttk.Button(self.window, text="Выход", command=self.exit_func, width=15, style='my.TButton')
        self.btn1.pack(side=tk.LEFT, pady=6, padx=40)

        # Создаем кнопку "Далее" и устанавливаем ее справа
        self.btn2 = ttk.Button(self.window, text="Далее", command=self.next_func, width=15, style='my.TButton')
        self.btn2.pack(side=tk.RIGHT, pady=6, padx=40)

        # Создаем стиль для кнопок
        self.style = ttk.Style()
        self.style.configure('my.TButton', background='#FFEE58', font=('Arial Black', 11))
        self.after_id = self.window.after(60000, self.exit_func)

    def exit_func(self):
        self.window.destroy()

    def next_func(self):
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
        self.window.destroy()
        self.main_window = self._window()
        self.main_window.window.mainloop()


start_window = StartWindow()
start_window.window.mainloop()
