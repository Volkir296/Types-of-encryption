from tkinter import *
from tkinter import ttk 
from VigenerFun import *

class App(Tk):

    def __init__(self):
        super().__init__()

        # Размер экрана
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        # Середину экрана
        w = w // 2 # X
        h = h // 2 # Y
        # Смещение от середины
        w = w - 200 
        h = h - 300

        self.geometry(f'400x200+{w}+{h}')
        self.title('The Vigener Cipher')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()