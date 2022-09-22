# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:34:51 2022

@author: lepidu
"""

from tkinter import *
import requests 




def openCageData(lat, long):
    # api-endpoint 
    URL = "https://api.opencagedata.com/geocode/v1/json"
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'q': str(lat) + ' ' + str(long),
              'key':'81b73effc59c427ea621bfeffa4a59d8'} 
      
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params=PARAMS) 
    
    # extracting data in json format 
    data = r.json() 
    
    #print (data.keys())
    #print(len(data['results']))
    #print(data['results'][0].keys())
    print(data['results'][0]['components'].keys())
    print(data['results'][0]['components']['country'])
    return data['results'][0]['components']['country']


textVar= openCageData(53.345995, -6.258893)

root = Tk()
root.geometry('800x500')

l = Label(root,text = textVar)
l.config(text="new Text")
l.pack()

root.mainloop()
