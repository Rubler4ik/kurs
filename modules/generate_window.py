import random
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror
import tkinter as tk


class GenerationWindow:
    def __init__(self, mainwindow, digit, frame, entries, canvas, on_close, icon=""):
        self._window = Toplevel(mainwindow)
        self._window.title("Генератор чисел")
        self._window.iconbitmap(default=icon)
        self._window.resizable(False, False)
        self.on_close = on_close
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
                          command=lambda: self._generate_numbers(digit, digit_count_entry))
        btn1.pack(anchor="nw", padx=20, pady=30, fill=X)
        self._window.update()
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_width() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_height() // 2}")
        self._window.grab_set()

    def _generate_numbers(self, digit, digit_count_entry):
        try:
            digit_count = int(digit_count_entry.get())
        except ValueError:
            showerror(title="Ошибка", message="Введено недопустимое значение. Пожалуйста, введите число.")
        else:
            self._generation(digit, digit_count)

    def _generation(self, digit, digit_count):
        for i in range(digit_count):
            random_digit = random.randint(0, digit)
            entry = tk.Entry(self._frame)
            entry.insert(0, f"{random_digit}")
            entry.grid(row=i % 10, column=i // 10, sticky="nsew")
            self._entries.append(entry)
        self._frame.update_idletasks()
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))
        self._window.destroy()
        if self.on_close:
            self.on_close()


