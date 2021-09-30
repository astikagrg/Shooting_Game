
from tkinter import *

def day():
    global logsin
    # main window for login and signup pages
    logsin = Tk()
    logsin.geometry("1280x720+0+0")  # resolution of the window
    logsin.title("G-Pass-LoginSignup")  # title of the window
    logsin.iconbitmap("Images/icon.ico")  # icon of the window
    logsin.resizable(False, False)  # stop the window from resizing
