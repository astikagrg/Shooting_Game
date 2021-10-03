import pygame
import random
import time
import sqlite3
from tkinter import *

global username, password
#creating a window
root=Tk()
root.geometry('800x600')
root.resizable(False,False)



def login():

    global bgimg,en_img, psw_img,bt_img, bt_img2
    login_fr = LabelFrame(root).place(x=0,y=0)
    #background image
    bgimg = PhotoImage(file='images/bg.png')
    bg_img = Label(login_fr, image=bgimg)
    bg_img.place(x=0, y=0)

    # box image place
    boximg = PhotoImage(file='images/rectanglelogin.PNG')
    box_img = Label(login_fr, image=boximg, bg='#030303', bd=0)
    box_img.place(x=179, y=108)

    # username entry
    en_img = PhotoImage(file='images/loginentry.png')
    ent_img=Label(login_fr, image=en_img,bg='#030303', bd=0)
    ent_img.place(x=240, y=131)

    username = StringVar()
    ent = Entry(login_fr, text=username ,bg='#FFBF3B',fg="#030303", bd=0, font=("Arial", 15))
    ent.place(x=260, y=147)

    #password entry
    psw_img = PhotoImage(file='images/loginentry.png')
    pw_img = Label(login_fr, image=psw_img, bg='#030303', bd=0)
    pw_img.place(x=240, y=220)

    password=StringVar()
    pw_ent=Entry(login_fr, text=password,bg='#FFBF3B',fg="#030303", bd=0, font=("Arial", 15))
    pw_ent.place(x=250,y=230)

    def signup():
       print("a")

    def login():
        print('3+2')

    bt_img = PhotoImage(file='images/play.png')
    but = Button(login_fr, command=signup(), image=bt_img, bg='#000000',bd=0).place(x=294, y=309)

    bt_img2 = PhotoImage(file='images/Signup.png')
    but2 = Button(login_fr, command=login(), image=bt_img2, bg='#000000',bd=0).place(x=480, y=378)



login()

root.mainloop()