from tkinter import *
from tkinter import ttk

def change(bt):
    bt['fg'] = '#000000'
    bt['activebackground'] = '#555555'
    bt['activeforeground'] = '#DCDCDC'

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
h = h - 300

root.geometry(f'400x620+{w}+{h}')
root.resizable(False, False)

#----------------------------------------------------------#

lent = Label().pack()
l1 = ttk.Label(text="The Caesar`s Cipher",font = "Arial 24", justify='center').pack()

#Encrypt
lent = Label().pack()
l2 = ttk.Label(text="Enter the message you want to encrypt :").pack()
ent1 = ttk.Entry(font= "Arial 16" , justify='center', width = '30').pack()
lent = Label().pack()
l3 = ttk.Label(text="Enter the shift :").pack()
ent2 = ttk.Entry(font= "Arial 16" , justify='center', width = '30').pack()
lent = Label().pack() 
btn1 = Button(text="Encrypt", font="Arial 16" ,width=30, height=2)
btn1.config(command=change(bt=btn1))
btn1.pack()

#Decrypt
lent = Label().pack()
l4 = ttk.Label(text="Enter the message you want to decrypt :").pack()
ent3 = ttk.Entry(font= "Arial 16" , justify='center', width = '30').pack()
lent = Label().pack()
l5 = ttk.Label(text="Enter the shift :").pack()
ent4 = ttk.Entry(font= "Arial 16" , justify='center', width = '30').pack()
lent = Label().pack() 
btn2 = Button(text="Decrypt", font="Arial 16" ,width=30, height=2)
btn2.config(command=change(bt=btn2))
btn2.pack()

#Output
lent = Label().pack()
result = ttk.Label(text="Result :", font='Arial 20').pack()
out_result = ttk.Entry(font= "Arial 16" , justify='center', width = '30').pack()

root.mainloop()