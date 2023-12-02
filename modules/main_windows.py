from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


class MainsWindows:
    def __init__(self, title, text, text2, text3, text4, text5, text6, image, text7, resizable, next_window,
                 icon="materials/sort-2_icon-icons.com_69583.ico"):
        self.main_window = None
        self._window = next_window
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap(default=icon)
        self.window.resizable(resizable, resizable)
        self.window.option_add("*tearOff", FALSE)
        if text != "":
            self.window.sort = Image.open(image).resize((100, 100))
            self.window.sort_tk = ImageTk.PhotoImage(self.window.sort)
            self.window["bg"] = "#FFCDD2"
            ttk.Label(self.window, text=text, font=('Arial Black', 10), justify="center", background="#FFCDD2",
                      padding=3).pack(anchor="n")

            ttk.Label(self.window, text=text2, font=('Arial Black', 9), justify="center", background="#FFCDD2",
                      padding=0).pack(anchor="center", padx=6)

            ttk.Label(self.window, text=text3, justify="center", background="#FFCDD2",
                      font=('Arial Black', 10),
                      padding=10).pack(anchor="center")

            ttk.Label(self.window, text=text4, justify="center", background="#FFCDD2", font=('Arial', 10),
                      padding=0).pack(anchor="center")

            ttk.Label(self.window, text=text5, justify="center", background="#FFCDD2",
                      font=('Arial Black', 10),
                      padding=0).pack(anchor="center")

            frame = tk.Frame(self.window, background="#FFCDD2")
            frame.pack(anchor="center", fill=X)
            ttk.Label(frame, image=self.window.sort_tk).pack(side='left', padx=50, pady=10)
            ttk.Label(frame, text=text6, background="#FFCDD2", justify=LEFT, font=('Arial', 10)).pack(anchor="e",
                                                                                                      padx=10, pady=10)

            ttk.Label(self.window, text=text7, background="#FFCDD2", justify=CENTER, font=('Arial Black', 10),
                      padding=0).pack(anchor="s", pady=5)

        self.window.update()
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2 - self.window.winfo_width() // 2}+"
            f"{self.window.winfo_screenheight() // 2 - self.window.winfo_height() // 2}")


