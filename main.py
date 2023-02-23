import time
import random as r
import tkinter
from tkinter import messagebox
from collections import Counter
from sort import *


#Konfiguracja GUI
root = tkinter.Tk()
#root.overrideredirect(True)

root.geometry("800x500")
root.configure(bg="#25283D")
root.resizable(False, False)
root.title("Proszę przyatakować")
#title_bar = tkinter.Frame(root, bg="#25283D", relief="raised", bd=0, highlightthickness=0)
#title_bar.pack(expand=1, fill=tkinter.X)
root.option_add('*Dialog.msg.font', 'Arvo 25')

#label
label = tkinter.Label(root, text="Porównanie QuickSort i MergeSort", height=2, width=30)
label.configure(font=("Rockwell", 20))
label.configure(bg="#EFD9CE")
label.pack(fill=tkinter.X)

#autor
tkinter.Label(root, text="Autorzy: Hubert Szarwiński, Jakub Izdebski", anchor="se", font=("Futura", 10),
              bg="#8F3985").place(x=542, y=480)

#button 1 2 3
b1 = tkinter.Button(root, text="Wczytaj z klawiatury", command=get_input, height=3, width=25, bg="#07BEB8")
b1.configure(font="arvo 12")
b1.pack()
b1.place(x=285, y=150)

b2 = tkinter.Button(root, text="Wczytaj z pliku\n (separator \',\')", command=chooseFile, height=3, width=25, bg="#07BEB8")
b2.configure(font="arvo 12")
b2.pack(expand=True)
b2.place(x=285, y=250)

b3 = tkinter.Button(root, text="Wczytaj 10000 losowych liczb", command=randList, height=3, width=25, bg="#07BEB8")
b3.configure(font="arvo 12")
b3.pack()
b3.place(x=285, y=350)

root.mainloop()

