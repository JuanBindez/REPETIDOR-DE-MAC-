'''
Copyright (c) 2022 Juan Carlos Bindez
This project is licensed under the MIT License.
'''

import os
import time
from tkinter import *
from tkinter import messagebox


def repete_10():
    file = 'mac.txt'
    os.remove(file)
    mac = input_mac.get()

    list = (mac, mac, mac, mac, mac, mac, mac, mac, mac, mac)

    with open("mac.txt", "w") as w:
        for item in list:
            w.write(item+'\n')
    messagebox.showinfo("Olá", "Foi Gerado o Arquivo mac.txt")


def repete_20():
    file = 'mac.txt'
    os.remove(file)
    mac = input_mac.get()

    list = (mac, mac, mac, mac, mac, mac, mac, mac, mac, mac,
     mac, mac, mac, mac, mac, mac, mac, mac, mac, mac,
    )

    with open("mac.txt", "w") as w:
        for item in list:
            w.write(item+'\n')
    messagebox.showinfo("Olá", "Foi Gerado o Arquivo mac.txt")


def repete_50():
    file = 'mac.txt'
    os.remove(file)
    mac = input_mac.get()

    list = (mac, mac, mac, mac, mac, mac, mac, mac, mac, mac,
    mac, mac, mac, mac, mac, mac, mac, mac, mac, mac,
    mac, mac, mac, mac, mac, mac, mac, mac, mac, mac,
    mac, mac, mac, mac, mac, mac, mac, mac, mac, mac,
    mac, mac, mac, mac, mac, mac, mac, mac, mac, mac,
    )

    with open("mac.txt", "w") as w:
        for item in list:
            w.write(item+'\n')
            
    messagebox.showinfo("Olá", "Foi Gerado o Arquivo mac.txt")



# interface
# X é para os lados e Y é altura
# lados x cima
window = Tk()
window.title("RepetidorDeMac")
window.geometry("400x200")
window['background'] = '#262626'# site to generate colors Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
window.resizable(False, False)# False para não responsivo e True para responsivo.

frame = Frame(window, width=400, height=140, bg="green")
frame.grid(row=0, column=0)
label = Label(window, text="Repetidor de Mac ", font=("Courier", 25), bg="green").place(x=50, y=30)

input_mac = (Entry(window, width=30))
input_mac.place(x=98, y=80)

button = Button(window, text="10x", command=repete_10, fg='white', bg='green')
button.place(x=75, y=150)

button = Button(window, text="20x", command=repete_20, fg='white', bg='green')
button.place(x=190, y=150)

button = Button(window, text="50x", command=repete_50, fg='white', bg='green')
button.place(x=310, y=150)

# interface


if __name__ == "__main__":
    window.mainloop()
