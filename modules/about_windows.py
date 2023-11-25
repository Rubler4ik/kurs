from tkinter import Toplevel, ttk, LEFT
from PIL import Image, ImageTk


class AboutWindow:
    def __init__(self, mainwindow, title, text, image, icon="materials/sort-2_icon-icons.com_69583.ico"):
        self._window = Toplevel(mainwindow)
        self._window.title(title)
        self._window["bg"] = "#FFCDD2"
        self._window.iconbitmap(default=icon)
        self._window.resizable(False, False)
        self._window.about = Image.open(image).resize((200, 220))
        self._window.about_tk = ImageTk.PhotoImage(self._window.about)
        self.label_image = ttk.Label(self._window, image=self._window.about_tk)
        self.label = ttk.Label(self._window, text=text, justify="center", background="#FFCDD2", font=('Arial', 11),
                               padding=8)

        self._window.grab_set()


class AboutAuthor(AboutWindow):
    def __init__(self, mainwindow):
        super().__init__(mainwindow, "Сведения об авторе",
                         "Автор: Гришко Дмитрий Игоревич\nГруппа: 10701222\nE-mail: dimagrishkoby@gmail.com ",
                         'materials/photo_2023-11-20_11-17-08.jpg')
        self.label_image.pack(anchor="n")
        self.label.pack(expand=True)
        self._window.update()
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_width() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_height() // 2}")


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
        self.label_image.pack(side=LEFT)
        self.label.pack(expand=True)
        self._window.update()
        self._window.geometry(
            f"+{self._window.winfo_screenwidth() // 2 - self._window.winfo_width() // 2}+"
            f"{self._window.winfo_screenheight() // 2 - self._window.winfo_height() // 2}")
