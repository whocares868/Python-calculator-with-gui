import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("450x600")
root.resizable(False, False)
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 30), width=18, state="disabled")
entry.place(relx=0.05, rely=0.05)



def onClick(number):
    global numbers1, numbers2
    getEntry = entry.get()
    print(getEntry)
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, getEntry+str(number))
    entry.config(state="disabled")
   
   



def calculate(calculation):
    global useFirstList, useSecondList
    getEntry = entry.get()
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, getEntry+calculation)
    entry.config(state="disabled")
    


def add():
    calculate("+")

def minus():
    calculate("-")

def multiply():
    calculate("*")

def divide():
    calculate("/")


def equal():
    getEntry = entry.get()
    print(getEntry)
    try:
        result = eval(getEntry)
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, result)
        entry.config(state="disabled")
        root.after(5000, clear)
    except:
        warning = messagebox.showinfo("Warning", "Please enter a proper calculation")
        clear()
    
   

def onClick7():
    onClick(7)

def onClick8():
    onClick(8)

def onClick9():
    onClick(9)

def onClick6():
    onClick(6)

def onClick5():
    onClick(5)

def onClick4():
    onClick(4)

def onClick3():
    onClick(3)

def onClick2():
    onClick(2)

def onClick1():
    onClick(1)

def onClick0():
    onClick(0)




def clear():
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.config(state="disabled")

    numbers1.clear()
    numbers2.clear()
    calculations.clear()

# First row
Button7 = tk.Button(root, text="7", font=("Arial", 45), width=3, command=onClick7)
Button7.place(relx=0, rely=0.2)

Button8 = tk.Button(root, text="8", font=("Arial", 45), width=3, command=onClick8)
Button8.place(relx=0.25, rely=0.2)

Button9 = tk.Button(root, text="9", font=("Arial", 45), width=3, command=onClick9)
Button9.place(relx=0.50, rely=0.2)

ButtonD = tk.Button(root, text="/", font=("Arial", 45), width=3, command=divide)
ButtonD.place(relx=0.75, rely=0.2)

# Second row


Button4 = tk.Button(root, text="4", font=("Arial", 45), width=3, command=onClick4)
Button4.place(relx=0, rely=0.394)

Button5 = tk.Button(root, text="5", font=("Arial", 45), width=3, command=onClick5)
Button5.place(relx=0.25, rely=0.394)


Button6 = tk.Button(root, text="6", font=("Arial", 45), width=3, command=onClick6)
Button6.place(relx=0.5, rely=0.394)


ButtonM = tk.Button(root, text="*", font=("Arial", 45), width=3, command=multiply)
ButtonM.place(relx=0.75, rely=0.394)


# Thrid row

Button1 = tk.Button(root, text="1", font=("Arial", 45), width=3, command=onClick1)
Button1.place(relx=0, rely=0.588)

Button2 = tk.Button(root, text="2", font=("Arial", 45), width=3, command=onClick2)
Button2.place(relx=0.25, rely=0.588)

Button3 = tk.Button(root, text="3", font=("Arial", 45), width=3, command=onClick3)
Button3.place(relx=0.5, rely=0.588)

ButtonMi = tk.Button(root, text="-", font=("Arial", 45), width=3, command=minus)
ButtonMi.place(relx=0.75, rely=0.588)



Button0 = tk.Button(root, text="0", font=("Arial", 45), width=3, command=onClick0)
Button0.place(relx=0, rely=0.782)

ButtonC = tk.Button(root, text=" ", font=("Arial", 45), width=3, command=clear)
ButtonC.place(relx=0.25, rely=0.782)

ButtonA = tk.Button(root, text="+", font=("Arial", 45), width=3, command=add)
ButtonA.place(relx=0.5, rely=0.782)

Equal = tk.Button(root, text="=", font=("Arial", 45), width=3, command=equal)
Equal.place(relx=0.75, rely=0.782)




root.mainloop()
