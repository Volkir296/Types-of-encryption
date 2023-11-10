from tkinter import *
from tkinter import ttk
from GenRandPrime import exit_gen
#from RSAFun import *

def event_gen_prime():
    
    p_fun = exit_gen()
    q_fun = exit_gen()

    prime_p_entry.delete(0, END)
    prime_p_entry.insert(0, p_fun)

    prime_q_entry.delete(0, END)
    prime_q_entry.insert(0, q_fun)


#root window
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
gen_prime_btn = Button(root, text="Generate prime", width= 16, command=event_gen_prime)
gen_prime_btn.grid(column= 2, row= 2, sticky='E', padx= 5, pady= 5)


root.mainloop()