import random
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror
import tkinter as tk


class GenerationWindow:
    def __init__(self, main_window, frame, entries, canvas, on_close, icon=""):
        self._window = Toplevel(main_window)
        self._window.title("Генератор чисел")
        self._window.iconbitmap(default=icon)
        self._window.resizable(False, False)
        self._window["bg"] = "#FFCDD2"
        self.on_close = on_close
        self._frame = frame
        self._entries = entries
        self._canvas = canvas
        self.digit_start = 0
        self.digit_end = 0
        gen1000 = "1000"
        gen10000 = "10000"
        gen100000 = "100000"
        gen_yours = "yours"
        self.label_start = ttk.Label(self._window, text="Введите начальное значение",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        self.enter_start = ttk.Entry(self._window)
        self.label_end = ttk.Label(self._window, text="Введите конечное значение",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        self.enter_end = ttk.Entry(self._window)
        self.Generation_value = StringVar(value=gen1000)
        self._choose()
        position = {"padx": 8, "pady": 6}
        self.btn_radio_1000 = Radiobutton(self._window, text="От 0 до 1000",
                           background="#FFCDD2", font="Arial,30", value=gen1000, command=self._choose,
                                              variable=self.Generation_value)

        self.btn_radio_10000 = Radiobutton(self._window, text="От 0 до 10000",
                            background="#FFCDD2", font="Arial,30",  value=gen10000, command=self._choose,
                                               variable=self.Generation_value)

        self.btn_radio_100000 = Radiobutton(self._window,text="От 0 до 100000",
                           background="#FFCDD2", font="Arial,30",  value=gen100000,
                                                command=self._choose,
                                                variable=self.Generation_value)

        self.btn_radio_yours = Radiobutton(self._window,
                             text="Свои значения",background="#FFCDD2", font="Arial,30",value=gen_yours,
                                               command=self._choose,
                                               variable=self.Generation_value)
        self.btn_radio_1000.grid(row=0, column=0, **position)
        self.btn_radio_10000.grid(row=0, column=1, **position)
        self.btn_radio_100000.grid(row=0, column=2, **position)
        self.btn_radio_yours.grid(row=0, column=3, **position)
        label1 = ttk.Label(self._window,
                           text="Введите количество гинерируемых чисел: ",
                           justify="center", background="#FFCDD2", font="Arial,30", padding=8)
        label1.grid(row=3, column=0, columnspan=4)

        digit_count_entry = Entry(self._window)
        digit_count_entry.grid(row=4, column=1,columnspan=2, padx=10, pady=5)

        btn1 = ttk.Button(self._window, text="Генерировать",
                          command=lambda: self._generate_numbers(self.digit_start, self.digit_end, digit_count_entry))
        btn1.grid(row=5, column=1,columnspan=2, padx=20, pady=20, sticky="ew")

        self._window.update()
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_width() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_height() // 2}")
        self._window.grab_set()

    def _generate_numbers(self, digit_start, digit_end, digit_count_entry):
        try:
            digit_count = int(digit_count_entry.get())
        except ValueError:
            showerror(title="Ошибка", message="Введено недопустимое значение. Пожалуйста, введите число.")
        else:
            self._generation(digit_start, digit_end, digit_count)

    def _choose(self):
        if self.Generation_value.get() == "1000":
            self.digit_end = 1000
            self.label_start.grid_forget()
            self.enter_start.grid_forget()
            self.label_end.grid_forget()
            self.enter_end.grid_forget()
        elif self.Generation_value.get() == "10000":
            self.digit_end = 10000
            self.label_start.grid_forget()
            self.enter_start.grid_forget()
            self.label_end.grid_forget()
            self.enter_end.grid_forget()
        elif self.Generation_value.get() == "100000":
            self.digit_end = 10000
            self.label_start.grid_forget()
            self.enter_start.grid_forget()
            self.label_end.grid_forget()
            self.enter_end.grid_forget()
        else:
            self.label_start.grid(row=1, column=1,padx= 3, pady= 4)
            self.enter_start.grid(row=1, column=2,padx= 3, pady= 4)
            self.label_end.grid(row=2, column=1,padx= 3, pady= 4)
            self.enter_end.grid(row=2, column=2,padx= 3, pady= 4)

    def _generation(self, digit_start, digit_end, digit_count):
        if self.Generation_value.get() == "yours":
            try:
                digit_start = int(self.enter_start.get())
                digit_end = int(self.enter_end.get())
            except ValueError:
                showerror("Ошибка", "Вы ввели не число")
        for i in range(digit_count):
            random_digit = random.randint(digit_start, digit_end)
            entry = tk.Entry(self._frame)
            entry.insert(0, f"{random_digit}")
            entry.grid(row=i % 10, column=i // 10, sticky="nsew")
            self._entries.append(entry)
        self._frame.update_idletasks()
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))
        self._window.destroy()
        if self.on_close:
            self.on_close()
