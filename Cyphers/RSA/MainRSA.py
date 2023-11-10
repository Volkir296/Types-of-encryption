from tkinter import *
from tkinter import ttk
from GenRandPrime import exit_gen
from GenRsaKey import generate_rsa_keys
#from RSAFun import *

def event_gen_prime(): #Генерация случайны простых чисел по кнопке
    
    p_fun = exit_gen()
    q_fun = exit_gen()

    prime_p_entry.delete(0, END)
    prime_p_entry.insert(0, p_fun)

    prime_q_entry.delete(0, END)
    prime_q_entry.insert(0, q_fun)

def event_gen_key(): #Генерация ключей по кнопке

    p_fun = int(prime_p_entry.get())
    q_fun = int(prime_q_entry.get())

    public_key, private_key = generate_rsa_keys(p_fun,q_fun)

    open_key_entry.delete(0, END)
    open_key_entry.insert(0, public_key)

    close_key_entry.delete(0, END)
    close_key_entry.insert(0, private_key)





#root window
root = Tk()
root.title('RSA')
# Размер экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
# Середину экрана
w = w // 2 # X
h = h // 2 # Y
# Смещение от середины
w = w - 200 
h = h - 300
root.geometry(f'400x300+{w}+{h}')
root.resizable(False, False)

#настройка сетки
root.columnconfigure(0, weight= 2)
root.columnconfigure(1, weight= 2)
root.columnconfigure(2, weight= 2)

#Описание простых чисел p и q
#p
prime_p_lab = Label(root, text="Prime 'p' ")
prime_p_lab.grid(column= 1, row=0, sticky='WE', padx= 5, pady=5)

prime_p_entry = ttk.Entry(root, justify='center')
prime_p_entry.grid(column= 1, row=1, sticky='WE', padx= 5, pady=5)

#q
prime_q_lab = Label(root, text="Prime 'q' ")
prime_q_lab.grid(column= 2, row=0, sticky='E', padx= 40, pady=5)

prime_q_entry = ttk.Entry(root, justify='center')
prime_q_entry.grid(column= 2, row=1, sticky='E', padx= 5, pady=5)

#Label 
prime_lab = Label(root, text="Enter prime digit: ")           
prime_lab.grid(column= 0, row=1, sticky='W', padx= 5, pady=5)

#Генератор случайных простых чисел p и q по кнопке, если пользователь не знает простые числа :D
gen_prime_btn = Button(root, text="Generate prime", width= 16, command=event_gen_prime) #command = Генерация случайны простых чисел по кнопке
gen_prime_btn.grid(column= 2, row= 2, sticky='E', padx= 5, pady= 5)
###

#lab_back
black_lab = ttk.Label(root, background='black')
black_lab.grid(columnspan=3, row= 3, sticky='WE', pady= 5)

#генерация открытого и закрытого ключей
#Открытый ключ
open_key_lab = Label(root, text="Open Key:")
open_key_lab.grid(column= 0, row= 4, sticky='W', padx= 5, pady= 5)

open_key_entry = ttk.Entry(root, justify='center')
open_key_entry.grid(column= 1, row= 4, sticky='WE', padx= 5, pady= 5)

#Закрытый ключ
close_key_lab = Label(root, text="Close Key:")
close_key_lab.grid(column= 0, row= 5, sticky='W', padx= 5, pady= 5)

close_key_entry = ttk.Entry(root, justify='center')
close_key_entry.grid(column= 1, row= 5, sticky='WE', padx= 5, pady= 5)

#event генерации ключей
gen_rsa_btn = ttk.Button(root, text='Generate Key', width= 16, command=event_gen_key)
gen_rsa_btn.grid(column= 2, row= 5, sticky='E', padx= 5, pady=5)
###

#lab_back
black_lab2 = ttk.Label(root, background='black')
black_lab2.grid(columnspan=3, row= 6, sticky='WE', pady= 5)


'''
#Message
message_lab = Label(root, text='Enter a message')
message_lab.grid(columnspan=3,row=4,sticky='WE')

message_entry = ttk.Entry(root, justify='center')
message_entry.grid(columnspan=3, row=5, sticky='WE')
'''




root.mainloop()