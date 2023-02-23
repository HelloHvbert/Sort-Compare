import random
import time
from datetime import datetime
from tkinter import messagebox, font
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import sys
from collections import Counter
import numbers

import random
import time


def CompareSort(listToSort):

    result = f"Ilość elementów w liście: {len(listToSort)}\n"
    print(f"Ilość elementów w liście: {len(listToSort)}\n")

    print(f"Lista przed sortowaniem:\n")
    print(listToSort)
    if len(listToSort) > 6:
        result += f"Lista przed sortowaniem:\n" \
                  f"[{listToSort[0]}, {listToSort[1]}, {listToSort[2]}, " \
                  f"... , {listToSort[-3]}, {listToSort[-2]}, {listToSort[-1]}]"
    else:
        result += "Lista przed sortowaniem:\n"+str(listToSort)+"\n"

    list1 = listToSort[:]
    list2 = listToSort[:]
    sortedList = sorted(listToSort)

    if len(sortedList) > 6:
        result += f"\nLista po sortowaniu:\n" \
                  f"[{sorted(listToSort)[0]}, {sorted(listToSort)[1]}, {sorted(listToSort)[2]}, " \
                  f"... , {sorted(listToSort)[-3]},  {sorted(listToSort)[-2]}, {sorted(listToSort)[-1]}]"
        print(f"\nLista po sortowaniu:\n"+
                  f"[{sorted(listToSort)[0]}, {sorted(listToSort)[1]}, {sorted(listToSort)[2]}, " +
                  f"... , {sorted(listToSort)[-3]},  {sorted(listToSort)[-2]}, {sorted(listToSort)[-1]}]")
    else:
        result += "Lista przed sortowaniem:\n"+str(sortedList)+"\n"
        print("Lista przed sortowaniem:\n"+str(sortedList)+"\n")


    print("\n\nMERGESORT:\n")
    result += "\nMERGESORT:\n"
    st = time.process_time()
    mergeSort(listToSort)
    et = time.process_time()
    print(f"Czas sortowania: {et - st} s")
    result += f"Czas sortowania: {et - st} s"
    #print(list0)

    print("\n\nQUICKSORT Z LOSOWYM WYBOREM ELEMENTU DZIELĄCEGO:\n")
    result += "\nQUICKSORT Z LOSOWYM WYBOREM ELEMENTU DZIELĄCEGO:\n"
    st = time.time()
    quickSort(list1, 0, len(list1) - 1)
    et = time.time()

    print(f"Czas sortowania: {et - st} s")
    result += f"Czas sortowania: {et - st} s"
    #print(list1)

    print("\n\nQUICKSORT Z MEDIANĄ:\n")
    result += "\nQUICKSORT Z MEDIANĄ:\n"
    st = time.time()
    quick_sort(list2, 0, len(list2) - 1)
    et = time.time()

    print(f"Czas sortowania: {et - st} s")
    result += f"Czas sortowania: {et - st} s"
    messagebox.showinfo("Wynik", result)
    #print(list2)
    #arr = [5,10,3]
    #print(arr)


def countDatatypes(arr):
    types = list(map(type, arr))
    if (types.count(int) > 0 or types.count(float) > 0) and (types.count(str) or types.count(chr) > 0 or types.count(complex) > 0):
        return False
    return True


def printList(array):
    if len(array) == 0:
        print("Lista jest pusta\n")


def listConvert(array):
    temp = list()
    for item in array:
        temp.append(int(item.strip()))
    return temp


def randList():
    listRand = [random.randint(0, 10000) for i in range(10000)]
    CompareSort(listRand)


def numbers_check(arr):
    for item in arr:
        if not item.isdigit():
            return False
    return True

#dane z pliku


def chooseFile(): #dane z pliku
    filetypes = ("text files", "*.txt")
    filename = ""
    filename = askopenfilename(title="Wybierz plik txt", filetypes=(("Text Files", "*.txt"),))

    if ".txt" not in filename:
        messagebox.showerror("Błąd", "Nie wybrano żadnego pliku")
        return

    try:
        file = open(filename, "r")
        fileList = file.read().split(',')
        if numbers_check(fileList):
            fileList = listConvert(fileList)
            CompareSort(fileList)
        else:
            print('A')
            CompareSort(fileList)
    except Exception as e:
        print(e)
        messagebox.showerror("Błąd","Nieprawidłowe dane")
        #print(fileList[-1])
    finally:
        file.close()


def check_list_for_numbers_and_text(lst):
    number = False
    text = False
    for item in lst:
        if isinstance(item, (int, float)):
            number = True
        elif isinstance(item, str):
            text = True
        if numbers and text:
            return True
    return False

#dane z klawiatury


def get_input():
    global root1
    root1 = tk.Tk()
    root1.geometry("400x200")
    root1.resizable(False, False)
    root1.configure(bg="#25283D")
    root1.title("Dane z klawiatury")

    # Create a label to prompt the user for input
    label = tk.Label(root1, text="Wpisz dane do posortowania, np. 21,52,37,24,...", font='Futura 12 bold',
                     bg="#EFD9CE", height=2)
    label.pack(fill=tk.X)

    # Create an Entry widget to accept the user's input
    entry = tk.Entry(root1, width=50)
    entry.pack()
    entry.place(x=48, y=100)
    entry.focus_set()

    # Create a button to submit the input
    button = tk.Button(root1, text="Sortuj", command=lambda: get_input_list(entry), width=6, height=1,
                       font='6', anchor="center")
    button.pack()
    button.place(x=160, y=150)

    # Run the Tkinter event loop
    root1.mainloop()


# Function to get the input value from the Entry widget and store it in a variable
def get_input_list(entry):
    input_value = entry.get()
    if input_value == "":
        messagebox.showerror("Błąd", "Nie podano danych")
        return
    root1.destroy()
    try:
        inputList = input_value.split(",")
        if numbers_check(inputList):
            fileList = listConvert(inputList)
            CompareSort(fileList)
        else:
            CompareSort(inputList)
    except:
        messagebox.showerror("Błąd", "Nieprawidłowe dane")


def getList():
    list0 = list()
    getType = input("d - 1000 los. liczb\nk - z klawiatury\np - z pliku\n")
    if getType == "d":
        list0 = [random.randint(0, 10000) for i in range(10000)]
    elif getType == "k":
        try:
            size = int(input("Podaj rozmiar: "))
        except ValueError:
            print("Rozmiar musi być liczbą\n")
            exit(-1)
        typ = input("Jaki typ danych chcesz sortować? s-str l-liczby\n")
        if typ == "s":
            for i in range(size):
                x = input()
                list0.append(x)
        elif typ == "l":
            try:
                for i in range(size):
                    x = int(input())
                    list0.append(x)
            except ValueError:
                print("Podano dane nie będące liczbą")
                exit(-1)
        else:
            print("Podano nieprawdiłowy typ")
            exit(-1)
    elif getType == "p":
        #wczytaj z pliku
        print("cccc")
    else:
        print("Podano nieprawdiłowy typ")
        exit(-1)
    return list0


def partition(arr, low, high):
    pivot = random.randint(low, high)

    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot = high

    for i in range(low, high):
        if arr[i] < arr[pivot]:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
    arr[low], arr[pivot] = arr[pivot], arr[low]
    return low


def quickSort(arr, low, high):
    if high <= low:
        return
    else:
        split = partition(arr, low, high)
        quickSort(arr, low, split-1)
        quickSort(arr, split+1, high)


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def mediana(arr, low, high):
    x = [0, 0, 0]
    #przypisuje tablicy x losowe indeksy
    for i in range(3):
        x[i] = random.randint(low, high)

    #sortuje indeksy w zaleznosci od zawartosci indeksu
    for i in range(1, 3):
        if arr[x[i]] < arr[x[i-1]]:
            x[i], x[i-1] = x[i-1], x[i]
    if arr[x[0]] > arr[x[1]]:
        x[0], x[1] = x[1], x[0]

    #zwracam indeks ktorego wartosc w tablicy jest mediana
    return x[1]


def partition2(arr, low, high):
    pivot = mediana(arr, low, high)

    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot = high

    #print(arr[pivot])
    for i in range(low, high):
        if arr[i] < arr[pivot]:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
    arr[low], arr[pivot] = arr[pivot], arr[low]
    return low


def quick_sort(arr, low, high):
    if high <= low:
        return
    else:
        split = partition2(arr, low, high)
        quick_sort(arr, low, split-1)
        quick_sort(arr, split+1, high)

