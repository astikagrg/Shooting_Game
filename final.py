from tkinter import *


def day():
    global login
    # main window for login and signup pages
    login = Tk()
    login.geometry("1280x720+0+0")  # resolution of the window
    login.title("Login")  # title of the window
    login.iconbitmap("Images/icon.ico")  # icon of the window
    login.resizable(False, False)
    # stop the window from resizing

    def log():
        login_fr=LabelFrame(login, width=1280,
                                 height=720,
                                 bd=0
                                 )
        login_fr.grid(row=0, column=0)

        username=StringVar

        username_ent = Entry(login_fr,
                         text=username,
                         font=("Arial", 15),
                         bd=0,
                         bg="#21BF99",
                         )
        username_ent.place(
            x=528,
            y=380,
        )

        def signup():
            # New frame for signup window
            signup_fr = LabelFrame(logsin,
                                      width=1280,
                                      height=720,
                                      bg="#2B958E",
                                      bd=0
                                      )
            signup_fr.grid(row=0, column=0)

            # Background of the signup frame
            bg_image = PhotoImage(file="Images/background.png")
            Label(signup_fr,
                  image=bg_image,
                  bg="#2B958E"
                  ).place(x=-3, y=-3)

        def login_c():
            """ Checks the login info from database """
            global username, password, logsin, a

            db = sqlite3.connect("Database.db")
            d = db.cursor()
            d.execute("SELECT *, oid FROM Signups")
            rec = d.fetchall()

            warn_login_text = StringVar()

            for i in rec:

                if i[1] == username.get() and i[2] == password.get():
                   print('Login successful')


                elif i[1] != username.get():

                    try:
                        a.destroy()
                        warn_login_text.set("Email not registered")
                        a = Label(login_fr, text=warn_login_text.get(),
                                  bg="#565050",
                                  font=("Arial", 10, "bold"),
                                  fg="#C09D47",
                                  bd=0,
                                  activeforeground="grey",
                                  activebackground="#565050",
                                  relief=FLAT, )
                        a.place(x=585, y=530)
                    except:
                        warn_login_text.set("Email not registered")
                        a = Label(login_fr, text=warn_login_text.get(),
                                  bg="#565050",
                                  font=("Arial", 10, "bold"),
                                  fg="#C09D47",
                                  bd=0,
                                  activeforeground="grey",
                                  activebackground="#565050",
                                  relief=FLAT, )
                        a.place(x=585, y=530)


            db.commit()
            db.close()

    log()

    login.mainloop()

day()
