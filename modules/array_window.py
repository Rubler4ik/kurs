import tkinter as tk
from tkinter import *


class ArrayWindow:
    def __init__(self, main_window, data_entries):
        self._window = Toplevel(main_window)
        self.main_window = main_window

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
            row = i % 10
            column = i // 10
            entry.insert(0, data_entries[i].get())
            entry.grid(row=row, column=column, sticky="nsew")
            self.entries.append(entry)
        self.rebuild_grid_array()
        self._window.update()

    def rebuild_grid_array(self):
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
