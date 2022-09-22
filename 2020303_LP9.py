# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:30:47 2022

@author: leisly
"""

from tkinter import *

root = Tk()
root.geometry("800x500")

bool_var = BooleanVar()

def action():
    print(bool_var.get())
    
cb1 = Checkbutton(root, text="CB option 1", command=action, variable=bool_var)
cb1.pack()



root.mainloop()