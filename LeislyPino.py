#Leisly Pino 2020303

#---------------Modules----------------- 
#Modules used for the development of the application
from tkinter import *
from tkinter import messagebox
from time import *
import requests
import sqlite3

#---------------Page Configuration------ 
    #Basic configuration of the application design
root = Tk()
root.title('App Leisly Pino 2020303')
root.config(bg='#f0f0f0')
root.geometry('1100x800')
menuBar = Menu(root)
root.config(menu=menuBar)

#---------------Functions Menu------------
    #Design and configuration of messages box
def addInfo():
    messagebox.showinfo("Saved information", "The information has been saved successfully.")

def exitApp():
    value = messagebox.askquestion("Exit", "Are you sure you want to exit the application?")
    if value == "yes":
        root.destroy()

def about():
    messagebox.showinfo("About the app", "This application was designed by Leisly Pino 2020303 during the summer of 2022 in the Python Programming subject taught by Professor Amilcar Aponte, at CCT College.")

    #Empty Label information
def cleanLabel():
    lbusiness.config(text="")
    lfinancial.config(text="")
    lsports.config(text="")

#---------------Database----------------
    #Create the NEWS database containing the 
    # DATANEWS table and its attributes
def connectionDB():

    myConnection = sqlite3.connect("NEWS")
    myCursor = myConnection.cursor()
    try:
        myCursor.execute('''
            CREATE TABLE DATANEWS (
            ID INTEGER PRYMARY KEY AUTO_INCREMENT,
            TYPE_NEWS VARCHAR(50),
            DATE VARCHAR(50),
            TIME VARCHAR(50),
            DESCRIPTION VARCHAR(100))
            ''')
        messagebox.showinfo("Database", "Database created successfully.")
    except:
        messagebox.showwarning("Existing database", "The database already exists in the system.")

    #Save and insert the elements to the 
    # DATANEWS table
def create():
    myConnection = sqlite3.connect("NEWS")
    myCursor = myConnection.cursor()
    myCursor.execute("INSERT INTO DATANEWS VALUES (NULL, '" + ltype.cget("text") +
        "','" + ldate.cget("text") +
        "','" + lhour.cget("text") +
        "','" + ldescription.cget("text") + "')")
    myConnection.commit()
    messagebox.showinfo("Database", "Information saved")

#---------------Date & Time-------------
    #Setting the date and time in real time
def getTime():
    hour = strftime('%H:%M:%S')
    day = strftime('%A')
    date = strftime('%d - %m - %y')

    lhour.config(text=hour)
    lday.config(text=day)
    ldate.config(text=date)

    lhour.after(1000, getTime)

#---------------News--------------------
    #Information is obtained from the 
    # News API where we show the user the 
    # title of the news with the topic of interest
def getBusiness():
    apiKey = "710a763b52a04c61ab064938bb29dc5c"
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="+apiKey
    news = requests.get(url).json()

    articles = news["articles"]

    myArticles = []
    myNews = ""
    for article in articles:
        myArticles.append(article["title"])
    
    for i in range(10):
        myNews = myNews + str(i+1) + ". " + myArticles[i] + "\n" +"\n"

    lbusiness.config(text=myNews)
    ltype.config(text="Business")
    ldescription.config(text="Business News")

def getSports():
    apiKey = "710a763b52a04c61ab064938bb29dc5c"
    url = "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey="+apiKey
    news = requests.get(url).json()

    articles = news["articles"]

    myArticles = []
    myNews = ""

    for article in articles:
        myArticles.append(article["title"])
    
    for i in range(10):
        myNews = myNews + str(i+1) + ". " + myArticles[i] + "\n" +"\n"

    lsports.config(text=myNews)
    ltype.config(text="Sports")
    ldescription.config(text="Sports News")
    

def getFinancial():
    apiKey = "710a763b52a04c61ab064938bb29dc5c"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+apiKey
    news = requests.get(url).json()

    articles = news["articles"]

    myArticles = []
    myNews = ""

    for article in articles:
        myArticles.append(article["title"])
    
    for i in range(10):
        myNews = myNews + str(i+1) + ". " + myArticles[i] + "\n" +"\n"

    lfinancial.config(text=myNews)
    ltype.config(text="Financial")
    ldescription.config(text="Financial News")

#--------------Frame----------------------
    #Frame is designed to display the date and time
myFrame = Frame(root)
myFrame.pack()
lwelcome = Label(myFrame, text="Welcome to the App", font=('Arial', 28, 'bold'))
lwelcome.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
lhour = Label(myFrame, font=('Arial', 12))
lhour.grid(row=1, column=0, padx=10, sticky='e')
lday = Label(myFrame, font=('Arial', 12))
lday.grid(row=1, column=1, padx=10, sticky='e')
ldate = Label(myFrame,  font=('Arial', 12))
ldate.grid(row=1, column=2, padx=10, sticky='e')

    #Frame2 is designed to display the information 
    # obtained by the News API and the button to
    # save the information to the database.
myFrame2 = Frame(root)
myFrame2.pack()
ldescription = Label(myFrame2)
ltype = Label (myFrame2)
lbusiness = Label(myFrame2, font=11, justify ="left", pady=20)
lbusiness.pack()
lfinancial = Label(myFrame2, font=11, justify ="left", pady=20)
lfinancial.pack()
lsports = Label(myFrame2, font=11, justify ="left", pady=20)
lsports.pack()
button = Button(root, font = 24, text= "Saved", command=create, pady=10)
button.pack()

#---------------Menu------------------
    #Design and configuration menu functions
homeMenu = Menu(menuBar, tearoff=0)
homeMenu.add_command(label="Connect", command=connectionDB)
homeMenu.add_command(label="Restart", command=cleanLabel)
newsMenu = Menu(menuBar, tearoff=0)
newsMenu.add_command(label="Business News", command=getBusiness)
newsMenu.add_command(label="Sports News", command=getSports)
newsMenu.add_command(label="Financial News", command=getFinancial)
exitMenu = Menu(menuBar, tearoff=0)
exitMenu.add_command(label="Exit", command=exitApp)
exitMenu.add_command(label="About", command=about) 

menuBar.add_cascade(label="Home", menu=homeMenu)
menuBar.add_cascade(label="News", menu=newsMenu)
menuBar.add_cascade(label="Exit", menu=exitMenu) 

    #Shows the date and time when starting the app
getTime()
root.mainloop()