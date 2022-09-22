# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:08:42 2022

@author: lepidu
"""

from tkinter import *

root = Tk()
root.geometry("800x500")



frame3 = LabelFrame(root, text="Yellow", bg="yellow")
frame3.pack(side=LEFT,expand=YES, fill=BOTH)

frame4 = LabelFrame(root, text="Pink", bg="pink")
frame4.pack(side=RIGHT,expand=YES, fill=BOTH)


frame = LabelFrame(root, text="Blue", bg="blue")
frame.pack(side=TOP,expand=YES, fill=BOTH)
mylabel = Label(frame, text="This is my sample text", bg="blue")
mylabel.pack()


frame2 = LabelFrame(root, text="Red", bg="red")
frame2.pack(side=BOTTOM,expand=YES, fill=BOTH)
mylabel2 = Label(frame2, text="This is my sample text", bg="red")
mylabel2.pack()

root.mainloop()
