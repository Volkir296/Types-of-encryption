from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Шифрование")
root.geometry("300x250+400+200")
root.update_idletasks()
root.resizable(False,False)
root.protocol("WM_DELETE_WINDOW", finish)
root.attributes("-toolwindow", True)

root.update()

root.mainloop()