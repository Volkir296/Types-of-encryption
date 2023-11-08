from tkinter import *
from tkinter import ttk
from Caesar import caesar_cipher, caesar_decipher



def change(bt): #Раскрашивание кнопки при нажатии
    bt['fg'] = '#000000'
    bt['activebackground'] = '#555555'
    bt['activeforeground'] = '#DCDCDC'

def show_message_encrypt():
    fun_mess = ent1.get()
    fun_shift = ent2.get()
    result = caesar_cipher(fun_mess,int(fun_shift))
    out_result.delete(0, END)
    out_result.insert(0, result)

def show_message_decrypt():
    fun_mess = ent3.get()
    fun_shift = ent4.get()
    result = caesar_decipher(fun_mess,int(fun_shift))
    out_result.delete(0, END)
    out_result.insert(0, result)
    
    

    

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

#h1 - label 
lent = Label().pack()
l1 = ttk.Label(text="The Caesar`s Cipher",font = "Arial 24", justify='center')
l1.pack()

#Encrypt
lent = Label().pack()
l2 = ttk.Label(text="Enter the message you want to encrypt :")
l2.pack()
ent1 = Entry(font= "Arial 16" , justify='center', width = '30')
ent1.pack()
lent = Label().pack()
l3 = ttk.Label(text="Enter the shift :")
l3.pack()
ent2 = ttk.Entry(font= "Arial 16" , justify='center', width = '30')
ent2.pack()
lent = Label().pack() 
btn1 = Button(text="Encrypt", font="Arial 16" ,width=30, height=2)
btn1.config(command=change(bt=btn1))
btn1.pack()

#Decrypt
lent = Label().pack()
l4 = ttk.Label(text="Enter the message you want to decrypt :")
l4.pack()
ent3 = ttk.Entry(font= "Arial 16" , justify='center', width = '30')
ent3.pack()
lent = Label().pack()
l5 = ttk.Label(text="Enter the shift :")
l5.pack()
ent4 = ttk.Entry(font= "Arial 16" , justify='center', width = '30')
ent4.pack()
lent = Label().pack() 
btn2 = Button(text="Decrypt", font="Arial 16" ,width=30, height=2)
btn2.config(command=change(bt=btn2))
btn2.pack()

#Output
lent = Label().pack()
result = ttk.Label(text="Result :", font='Arial 20')
result.pack()
out_result = ttk.Entry( font= "Arial 16" , justify='center', width = '30' )
out_result.pack()

#Event
btn1.config(command=show_message_encrypt)
btn2.config(command=show_message_decrypt)


root.mainloop()

#----------------------------------------------------------#

