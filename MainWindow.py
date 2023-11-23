from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


class MainsWindows:
    def __init__(self, title, text, text2, text3, text4, text5, text6, image, text7, resizable,
                 icon="materials/sort-2_icon-icons.com_69583.ico"):
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap(default=icon)
        self.window.resizable(resizable, resizable)
        self.window.option_add("*tearOff", FALSE)
        if text != "":
            self.window.sort = Image.open(image).resize((100, 100))
            self.window.sort_tk = ImageTk.PhotoImage(self.window.sort)
            self.window["bg"] = "#FFCDD2"
            label = ttk.Label(self.window, text=text, font=('Arial Black', 10), justify="center", background="#FFCDD2",
                              padding=3)
            label.pack(anchor="n")
            label2 = ttk.Label(self.window, text=text2, font=('Arial Black', 9), justify="center", background="#FFCDD2",
                               padding=0)
            label2.pack(anchor="center")
            label3 = ttk.Label(self.window, text=text3, justify="center", background="#FFCDD2",
                               font=('Arial Black', 10),
                               padding=10)
            label3.pack(anchor="center")
            label4 = ttk.Label(self.window, text=text4, justify="center", background="#FFCDD2", font=('Arial', 10),
                               padding=0)
            label4.pack(anchor="center")
            label5 = ttk.Label(self.window, text=text5, justify="center", background="#FFCDD2",
                               font=('Arial Black', 10),
                               padding=0)
            label5.pack(anchor="center")

            frame = tk.Frame(self.window, background="#FFCDD2")
            frame.pack(anchor="center", fill=X)
            image_label = ttk.Label(frame, image=self.window.sort_tk)
            image_label.pack(side='left', padx=50, pady=10)
            label6 = ttk.Label(frame, text=text6, background="#FFCDD2", justify=LEFT, font=('Arial', 10))
            label6.pack(anchor="e", padx=10, pady=10)
            label7 = ttk.Label(self.window, text=text7, background="#FFCDD2", justify=CENTER, font=('Arial Black', 10),
                               padding=0)
            label7.pack(anchor="s", pady=5)

        self.window.update()
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2 - self.window.winfo_width() // 2}+"
            f"{self.window.winfo_screenheight() // 2 - self.window.winfo_height() // 2}")
