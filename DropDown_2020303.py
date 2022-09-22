# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 15:17:11 2022

@author: leisly
"""


from tkinter import *

root = Tk()
root.geometry("800x500")

string_var = StringVar()

def action(selection):
    print(selection)
    
options = ["Blue", "Pink", "Yellow", "Red", "Orange", "Magenta"]

drop = OptionMenu(root, string_var, *options, command=action)
drop.pack()


root.mainloop()