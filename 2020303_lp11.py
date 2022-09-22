# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:22:31 2022

@author: leisly
"""

from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Leisly Pino 2020303')
root.geometry("400x400")



try:
    api_request = requests.get("https://newsapi.org/v2/top-headlines/sources?category=business,sports,financial&apiKey=710a763b52a04c61ab064938bb29dc5c")
    api = json.loads(api_request.content)
    #category = api[0]['category']
    #language = api[0]['language']
    #description = api[0]['description']
except Exception as e:
    api = "We can not with the website"

myLabel = Label(root, text=api, font=("Arial", 12))
myLabel.pack()

root.mainloop()