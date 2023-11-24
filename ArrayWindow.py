import tkinter as tk


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
            entry.grid()
            self.entries.append(entry)
        self._rebuild_grid()


    def _rebuild_grid(self):
        for i, entry in enumerate(self.entries):
            row = i % 10
            column = i // 10
            entry.grid(row=row, column=column, sticky="nsew")
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
