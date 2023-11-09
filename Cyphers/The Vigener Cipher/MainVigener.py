from tkinter import *
from tkinter import ttk 
from VigenerFun import vigenere_cipher

def change(bt): #Раскрашивание кнопки при нажатии
    bt['fg'] = '#000000'
    bt['activebackground'] = '#555555'
    bt['activeforeground'] = '#DCDCDC'

def click_button_one(): #Флаг шифрования
    mode = 'encrypt'
    action_to_encrypt(mode)

def click_button_two(): #Флаг дешифрования
    mode = 'decrypt'
    action_to_encrypt(mode)

def action_to_encrypt(fun_mode:str): #Результат = результат Виженера
    fun_word = str(one_word_entry.get())
    fun_key = str(one_key_entry.get())
    fun_result = vigenere_cipher(fun_word, fun_key, fun_mode)
    result_out.delete(0, END)
    result_out.insert(0, fun_result)

root = Tk()    
# Размер экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
# Середину экрана
w = w // 2 # X
h = h // 2 # Y
# Смещение от середины
w = w - 200 
h = h - 300

root.geometry(f'400x230+{w}+{h}')
root.title('The Vigener Cipher')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=4)

#Word to encrypt//decrypt
one_word_lab = ttk.Label(root, text="Enter the word :", font = "Arial 24")
one_word_lab.grid(column=0, row=0, sticky='W', padx=5, pady=10)

one_word_entry = ttk.Entry(root)
one_word_entry.grid(column=1, row=0, sticky='WE', padx=5, pady=10)

#Key
one_key_lab = ttk.Label(root, text="Enter the key :", font = "Arial 24")
one_key_lab.grid(column=0, row=1, sticky='W', padx=5, pady=10)

one_key_entry = ttk.Entry(root)
one_key_entry.grid(column=1, row=1, sticky='WE', padx=5, pady=10)

#button ecrypt//decrypt
btn1 = Button(root, text="Ecrypt", font= "Arial 18", command=click_button_one,width=10)
btn1.grid(column=0,row=3, sticky='W', padx= 5, pady= 5)
btn1.config(command=change(bt=btn1))

btn2 = Button(root, text="Decrypt", font= "Arial 18", command=click_button_two,width=10)
btn2.grid(column=1,row=3, sticky='E', padx= 5, pady= 5)
btn2.config(command=change(bt=btn2))

#Result
result_lab = ttk.Label(root, text="Result: ", font = "Arial 24")
result_lab.grid(column=0, row=4, sticky='W', padx=5, pady=10)

result_out = ttk.Entry(root)
result_out.grid(column=1, row=4, sticky='WE', padx=5, pady=10)

root.mainloop()