from tkinter import *
from tkinter import ttk

#----------------------------------------------#
root = Tk()
root.title('XOR')

# Размер экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# Середину экрана
w = w // 2 # X
h = h // 2 # Y

# Смещение от середины
w = w - 200 
h = h - 300

root.geometry(f'400x620+{w}+{h}')
root.resizable(False, False)
#----------------------------------------------#





root.mainloop()