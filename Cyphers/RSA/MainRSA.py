from tkinter import *
from tkinter import ttk
from GenRandPrime import exit_gen
from GenRsaKey import generate_keypair
from RSAFun import encrypt, decrypt

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

    public_key, private_key = generate_keypair(p_fun,q_fun)

    open_key_entry.delete(0, END)
    open_key_entry.insert(0, public_key)

    public_key_entry.delete(0, END)
    public_key_entry.insert(0, public_key)

    close_key_entry.delete(0, END)
    close_key_entry.insert(0, private_key)

def event_to_encrypt():

    mess_fun = message_entry.get()
    public_fun = public_key_entry.get()
    
    encrypt_mess_fun = encrypt(public_fun, mess_fun)

    encrypt_entry.delete(0, END)
    encrypt_entry.insert(0, encrypt_mess_fun)

    encrypted_text_message= ''.join(chr(char)for char in encrypt_mess_fun)
    sym_entry.delete(0, END)
    sym_entry.insert(0, encrypted_text_message)


def event_to_decrypt():

    mess_fun = encrypt_message_entry.get()
    private_fun = private_key_entry.get()
    
    decrypt_mess_fun = decrypt(private_fun, mess_fun)

    decrypt_message_entry.delete(0, END)
    decrypt_message_entry.insert(0, decrypt_mess_fun)


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
root.geometry(f'400x700+{w}+{h}')
root.resizable(False, False)

#настройка сетки
root.columnconfigure(0, weight= 2)
root.columnconfigure(1, weight= 2)
root.columnconfigure(2, weight= 2)

#lab_back
black_lab = ttk.Label(root, background='black')
black_lab.grid(columnspan=3, row= 0, sticky='WE')

#Описание простых чисел p и q
#p
prime_p_lab = Label(root, text="Prime 'p' ")
prime_p_lab.grid(column= 1, row=1, sticky='WE', padx= 5, pady=5)

prime_p_entry = ttk.Entry(root, justify='center')
prime_p_entry.grid(column= 1, row=2, sticky='WE', padx= 5, pady=5)

#q
prime_q_lab = Label(root, text="Prime 'q' ")
prime_q_lab.grid(column= 2, row=1, sticky='E', padx= 40, pady=5)

prime_q_entry = ttk.Entry(root, justify='center')
prime_q_entry.grid(column= 2, row=2, sticky='E', padx= 5, pady=5)

#Label 
prime_lab = Label(root, text="Enter prime digit: ")           
prime_lab.grid(column= 0, row=2, sticky='W', padx= 5, pady=5)

#Генератор случайных простых чисел p и q по кнопке, если пользователь не знает простые числа :D
gen_prime_btn = Button(root, text="Generate prime", width= 16, command=event_gen_prime) #command = Генерация случайны простых чисел по кнопке
gen_prime_btn.grid(column= 2, row= 3, sticky='E', padx= 5, pady= 5)
###

#lab_back
black_lab = ttk.Label(root, background='black')
black_lab.grid(columnspan=3, row= 4, sticky='WE', pady= 5)

#генерация открытого и закрытого ключей
#Открытый ключ
open_key_lab = Label(root, text="Public Key:")
open_key_lab.grid(column= 0, row= 5, sticky='W', padx= 5, pady= 5)

open_key_entry = ttk.Entry(root, justify='center')
open_key_entry.grid(column= 1, row= 5, sticky='WE', padx= 5, pady= 5)

#Закрытый ключ
close_key_lab = Label(root, text="Private Key:")
close_key_lab.grid(column= 0, row= 6, sticky='W', padx= 5, pady= 5)

close_key_entry = ttk.Entry(root, justify='center')
close_key_entry.grid(column= 1, row= 6, sticky='WE', padx= 5, pady= 5)

#event генерации ключей
gen_rsa_btn = ttk.Button(root, text='Generate Key', width= 16, command=event_gen_key)
gen_rsa_btn.grid(column= 2, row= 6, sticky='E', padx= 5, pady=5)
###

#lab_back
black_lab = ttk.Label(root, background='black')
black_lab.grid(columnspan=3, row= 7, sticky='WE', pady= 5)

#Message
message_lab = Label(root, text='Enter a message to encrypt')
message_lab.grid(columnspan=3,row=8,sticky='WE')

message_entry = ttk.Entry(root, justify='center')
message_entry.grid(columnspan=3, row=9, sticky='WE')

#Event encrypt
encrypt_btn = ttk.Button(root, text='Encrypt', command=event_to_encrypt)
encrypt_btn.grid(columnspan=3, row=11, sticky='WE', pady= 10)

#Encrypt message 
encrypt_message_lab = ttk.Label(root, text='Encrypt message')
encrypt_message_lab.grid(column=1, columnspan=2,row=12,sticky='WE', padx= 40)

public_message_lab = ttk.Label(root, text='Enter publick key:')
public_message_lab.grid(column=0, columnspan=2,row=10,sticky='WE',padx= 5 ,pady= 5)

public_key_entry = ttk.Entry(root, justify='center')
public_key_entry.grid(column=1, columnspan=2,row=10,sticky='WE',padx= 5 ,pady= 5)

encrypt_entry = ttk.Entry(root, justify='center')
encrypt_entry.grid(columnspan=3, row=13, sticky='WE')

#lab_back
black_lab = ttk.Label(root, background='black')
black_lab.grid(columnspan=3, row= 14, sticky='WE', pady= 5)

#Decrypt message
encrypt_message_lab = Label(root, text='Enter encrypt message to decrypt')
encrypt_message_lab.grid(columnspan=3,row=15,sticky='WE')

encrypt_message_entry = ttk.Entry(root, justify='center')
encrypt_message_entry.grid(columnspan=3, row=16, sticky='WE')

private_message_lab = ttk.Label(root, text='Enter private key:')
private_message_lab.grid(column=0, columnspan=2,row=17,sticky='WE',padx= 5 ,pady= 5)

private_key_entry = ttk.Entry(root, justify='center')
private_key_entry.grid(column=1, columnspan=2,row=17,sticky='WE',padx= 5 ,pady= 5)

#decrypt button
decrypt_btn = ttk.Button(root, text='Decrypt', command=event_to_decrypt)
decrypt_btn.grid(columnspan=3, row=18, sticky='WE', pady= 10)

decrypt_message_lab = ttk.Label(root, text='Decrypt message')
decrypt_message_lab.grid(column=1, columnspan=2,row=19,sticky='WE', padx= 40)

decrypt_message_entry = ttk.Entry(root, justify='center')
decrypt_message_entry.grid(columnspan=3, row=20, sticky='WE')

#lab_back
black_lab = ttk.Label(root, background='black')
black_lab.grid(columnspan=3, row= 21, sticky='WE', pady= 5)

sym_lab = Label(root, text= "Encrypted symbolic message")
sym_lab.grid(columnspan=3, row=22, sticky='WE', padx= 5, pady= 5)

sym_entry = ttk.Entry(root, justify='center')
sym_entry.grid(columnspan=3, row= 23, sticky='WE', padx= 5, pady= 5)

black_lab = ttk.Label(root, background='black')
black_lab.grid(columnspan=3, row= 24, sticky='WE', pady= 5)

root.mainloop()