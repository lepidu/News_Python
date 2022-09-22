# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:24:02 2022

@author: lepidu
"""

from tkinter import *

def clicked():
    print("button is clicked")

root = Tk()

root.title("Whatever title here")
root.geometry("800x500")

# my_label = Label(root, text="Whatever text I want")
# my_label.pack()

my_button = Button(root, text="Click me", command=clicked, bg='green')
# my_button.pack(side=RIGHT,  padx=100, pady=100)
my_button.grid(row=0, column=0)

my_button2 = Button(root, text="Click me2", command=clicked)
# my_button2.pack(side=RIGHT)
my_button2.grid(row=1, column=1)

my_button3 = Button(root, text="Click me3", command=clicked)
# my_button3.pack(side=RIGHT)
my_button3.grid(row=2, column=2)


root.mainloop()




