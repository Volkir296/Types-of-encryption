from tkinter import *
from tkinter import ttk
from XORFun import Dec_to_Bin, XOR_Fun

def XOR_click_event(): #Ивент для btn1
    fun_digit = Dec_to_Bin(int(digit_entry.get()))
    fun_key = Dec_to_Bin(int(key_entry.get()))
    digit_bin_lab["text"] = fun_digit
    key_bin_lab["text"] = fun_key
    fun_digit_int = int(digit_entry.get())
    fun_key_int = int(key_entry.get())
    fun_result = XOR_Fun(fun_digit_int,fun_key_int)
    result_out.delete(0, END)
    result_out.insert(0, fun_result)
    fun_result = Dec_to_Bin(fun_result)
    result_bin_lab["text"]  = fun_result
    
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
root.geometry(f'300x200+{w}+{h}')
root.resizable(True, False)

#настройка сетки
root.columnconfigure(0, weight= 1)
root.columnconfigure(1, weight= 2)
root.columnconfigure(2, weight= 6)

# Designations
dec_lab = ttk.Label(root, text="DEC")
dec_lab.grid(column=1, row=0, sticky='WE',padx= 35, pady= 5)

bin_lab = ttk.Label(root, text="BIN")
bin_lab.grid(column=2, row=0, sticky='E',padx= 42, pady= 5)

# Digit to encrypt
digit_lab = ttk.Label(root, text="Enter digit :")
digit_lab.grid(column=0, row=1, sticky='W',padx= 5, pady= 5)

digit_entry = ttk.Entry(root,width= 2)
digit_entry.grid(column=1, row=1, sticky='WE', padx= 5, pady= 5)

digit_bin_lab = ttk.Label(root, text="NONE")
digit_bin_lab.grid(column=2, row=1, sticky='E',padx= 35, pady= 5)

#Key
key_lab = ttk.Label(root, text="Enter key :")
key_lab.grid(column = 0, row = 2, sticky = 'W',padx = 5, pady = 5)

key_entry = ttk.Entry(root,width= 2)
key_entry.grid(column = 1, row= 2, sticky = 'WE', padx = 5, pady = 5)

key_bin_lab = ttk.Label(root, text="NONE")
key_bin_lab.grid(column = 2, row = 2, sticky = 'E',padx = 35, pady = 5)

#button
btn1 = ttk.Button(root,text="RUN", command=XOR_click_event) #command => event
btn1.grid(column = 1,row = 3, sticky = 'WE', padx = 5, pady = 5)

#result
result_lab = ttk.Label(root, text="Result :")
result_lab.grid(column = 0, row = 4, sticky = 'W', padx = 5, pady = 5)

result_out = ttk.Entry(root,width= 2)
result_out.grid(column = 1,row = 4, sticky = 'WE', padx = 5, pady = 5)

result_bin_lab = ttk.Label(root, text="NONE")
result_bin_lab.grid(column=2, row= 4, sticky = 'E',padx = 35, pady = 5)

root.mainloop()