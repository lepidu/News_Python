# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 15:22:37 2022

@author: leisly
"""

from tkinter import *

root = Tk()
root.title("My GUI")


screen = Entry(root, width=40 )
screen.pack( padx=10, pady =10)
screen.insert(0,"0")

keyboard = Frame(root)
keyboard.pack(expand=YES, padx=10, pady = 10)

total = 0

def clicked(x):
    if (screen.get() == "0"):
        screen.delete(0,"end")
    #len(screen.get())
    screen.insert( len(screen.get()) , x)

def clear():
    screen.delete(0, 'end')
    screen.insert(0,"0")
    global total
    total = 0
    
def add():
    global total
    total = total + int(screen.get())
    screen.delete(0, 'end')
    screen.insert(0,"0")

def result():
    add()
    global total
    screen.delete(0, 'end')
    screen.insert(0, total)
    total = 0

seven = Button (keyboard, text="7",command = lambda: clicked("7"), padx=30, pady=30)
seven.grid(row=0, column=0)

eight = Button (keyboard, text="8",command = lambda: clicked("8"), padx=30, pady=30)
eight.grid(row=0, column=1)

nine = Button (keyboard, text="9",command = lambda: clicked("9"), padx=30, pady=30)
nine.grid(row=0, column=2)

four = Button (keyboard, text="4",command = lambda: clicked("4"), padx=30, pady=30)
four.grid(row=1, column=0)

five = Button (keyboard, text="5",command = lambda: clicked("5"), padx=30, pady=30)
five.grid(row=1, column=1)

six = Button (keyboard, text="6",command = lambda: clicked("6"), padx=30, pady=30)
six.grid(row=1, column=2)

one = Button (keyboard, text="1",command = lambda: clicked("1"), padx=30, pady=30)
one.grid(row=2, column=0)

two = Button (keyboard, text="2",command = lambda: clicked("2"), padx=30, pady=30)
two.grid(row=2, column=1)

three = Button (keyboard, text="3",command = lambda: clicked("3"), padx=30, pady=30)
three.grid(row=2, column=2)

zero = Button (keyboard, text="0",command = lambda: clicked("0"), padx=30, pady=30)
zero.grid(row=3, column=0)

clear = Button (keyboard, text="C",command = clear, padx=67, pady=30)
clear.grid(row=3,  column=1, columnspan = 2)

plus = Button (keyboard, text="+",command = add, padx=30, pady=30)
plus.grid(row=4, column=0)

equals = Button (keyboard, text="=",command = result,padx=67, pady=30)
equals.grid(row=4,  column=1, columnspan = 2)

root.mainloop()
