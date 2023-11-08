from tkinter import *
from tkinter import ttk


#----------------------------------------------------------#
root = Tk()

root.title('The Caesar`s Cipher')

# Размер экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# Середину экрана
w = w // 2 # X
h = h // 2 # Y

# Смещение от середины
w = w - 200 
h = h - 200

root.geometry(f'400x200+{w}+{h}')
root.resizable(False, False)

#----------------------------------------------------------#

l1 = ttk.Label(text="The Caesar`s Cipher", font = "Arial 24", justify='center').pack()

ent1 = ttk.Entry(justify='center', width = '60').pack()


root.mainloop()