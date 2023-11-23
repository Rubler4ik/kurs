from tkinter import ttk
from tkinter import *


class MainsWindows:
    def __init__(self, title, text, text2, text3,resizable, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap(default=icon)
        self.window.resizable(resizable, resizable)
        self.window.option_add("*tearOff", FALSE)
        if text != "":
            self.window["bg"] = "#FFCDD2"
            label = ttk.Label(self.window, text=text, justify="center", background="#FFCDD2",font="Helvetica,40",
                              padding=8)
            label.pack(anchor="n")
            label2= ttk.Label(self.window, text=text2,justify="center", background="#FFCDD2", font="Helvetica,30",
                              padding=8)
            label2.pack(expand=True)
            label3 = ttk.Label(self.window, text=text3, justify="center", background="#FFCDD2", font="Arial,30",
                               padding=8)
            label3.pack(expand=True)

        self.window.update()
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2 - self.window.winfo_width() // 2}+"
            f"{self.window.winfo_screenheight() // 2 - self.window.winfo_height() // 2}")
