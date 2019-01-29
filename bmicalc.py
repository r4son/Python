#! /usr/local/bin/python3

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import getdouble


root = Tk()
Frame(root, bg="grey").pack()
root.title("BMI Calculator")
root.minsize(300,400)
root.geometry("300x400")

#! Python GUI Functions
def callState():
    weight = float(E2.get())
    height = float(E1.get())
    new_height = height * height
    bmi = float(weight / new_height)
    if bmi > 10 and bmi < 60:
        if bmi > 0 and bmi < 18.5:
            return "You are underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            return "You are normal weight"
        elif bmi >= 25 and bmi <= 29.9:
            return "You are overweight"
        elif bmi >= 30 and bmi <= 34.9:
            return "You are obese"
        elif bmi >= 35 and bmi <= 39.9:
            return "You have obesity grade II"
        elif bmi >= 40:
            return "You have obesity grade III"
    else:
        return "Invalid entries"

def calculate():
    name = E0.get()
    weight = float(E2.get())
    height = float(E1.get())
    new_height = height * height
    bmi = float(weight / new_height)
    your_bmi = "Hello, ", name, "Your BMI is: %.2f " % bmi, "\n", callState(),
    msg = messagebox.showinfo("Ergebnis", your_bmi)


#! Python GUI
welcomelabel = Label(root, text="BMI Calc coded by Krisztian Cserge © 2019")
welcomelabel.pack()
L0 = Label(root, text="Name")
L0.pack()
E0 = Entry(root, bd=5, exportselection=0,)
E0.pack()
L1 = Label(root, text="Groeße")
L1.pack()
E1 = Entry(root, bd=5, exportselection=0,)
E1.pack()
L2 = Label(root, text="Gewicht")
L2.pack()
E2 = Entry(root, bd=7, exportselection=0)
E2.pack()
B = Button(root, text = "Calculate", command=calculate)
B.place(x=110, y = 225)

root.mainloop()
