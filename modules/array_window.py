import tkinter as tk
from tkinter import *


class ArrayWindow:
    def __init__(self, mainwindow, data_entries, rebuild_grid):
        self._window = Toplevel(mainwindow)
        self.mainwindow = mainwindow
        self.rebuild_grid = rebuild_grid
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
        self.rebuild_grid()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
