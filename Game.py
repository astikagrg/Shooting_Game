import pygame
import random
import time
import sqlite3
from tkinter import *

global username, password
# creating a window
root = Tk()
root.geometry('800x600')
root.resizable(False, False)



def game2():

    global programIcon
    # General setup
    pygame.init()

    clock = pygame.time.Clock()

    # color
    BLACK = (0, 0, 0)

    # Game window
    wn_width = 600
    wn_height = 500
    wn = pygame.display.set_mode((wn_width, wn_height))
    pygame.display.set_caption('Shoot asteroids')
    programIcon = pygame.image.load('icon.ico')
    pygame.display.set_icon(programIcon)

    # images and sounds
    bg_img = pygame.image.load('images/background.jpg')
    bg_img = pygame.transform.scale(bg_img, (600, 600))
    target_img = pygame.image.load('images/asteroid2.png')
    target_img2 = pygame.image.load('images/asteroid 1.png')
    crosshair_img = pygame.image.load('images/crosshair.png')
    gun_sound = pygame.mixer.Sound('sounds/laser.wav')
    pygame.mouse.set_visible(False)

    # Database sqLite3

    conn = sqlite3.connect("Score.db")
    c = conn.cursor()

    c.execute(
        '''CREATE TABLE IF NOT EXISTS block(
            score int

        )'''
    )
    conn.commit()
    conn.close()

    def score_board(score):
        global usernam1
        font = pygame.font.Font('freesansbold.ttf', 35)
        text = font.render('Score ' + str(score), True, (255, 255, 255))
        wn.blit(text, (5, 10))

        font1 = pygame.font.Font('freesansbold.ttf', 35)
        text2 = font1.render('Score ' +'25', True, (255, 255, 255))
        wn.blit(text, (5, 10))

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = crosshair_img
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.center = pygame.mouse.get_pos()

    class Target(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            ran_no = random.randint(1, 2)
            if ran_no == 1:
                self.image = target_img
            else:
                self.image = target_img2
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, wn_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randrange(1, 2)
            self.speedx = random.randrange(-1, 2)

        def update(self):
            global score, usernam1
            self.rect.x = self.rect.x + self.speedx
            self.rect.y = self.rect.y + self.speedy

            if self.rect.right < 0 or self.rect.left > wn_width:
                self.rect.x = random.randint(0, wn_width - self.rect.width)
                self.rect.y = random.randint(-100, -40)
                self.speedy = random.randint(1, 4)
                self.speedx = random.randint(-1, 2)

            if self.rect.top > wn_height:  # game over
                font = pygame.font.Font(None, 80)
                text = font.render('Game Over', True, BLACK)
                wn.blit(text, (150, 150))
                pygame.display.flip()
                time.sleep(2)

                db = sqlite3.connect("Score.db")
                c = db.cursor()
                c.execute(
                    f'''SELECT * FROM user_score WHERE :usernam={ent.get}'''
                )
                d = c.fetchall()
                e = d[0]
                e_0 = e[0]
                e_1 = e[1]
                e_2 = e[2]
                c.execute(f''' DElETE FROM user_score WHERE :usernam={usernam1}''')
                db.commit()
                if score > e_1:
                    e_1 = score

                c.execute(
                    'INSERT INTO user_score VALUES (:usernam,:score, :password)',
                    {
                        "usernam": e_0,
                        "score": e_1,
                        "password": e_2

                    },

                )
                db.commit()

    def game_loop():
        # Player
        player = Player()
        player_group = pygame.sprite.Group()
        player_group.add(player)

        # Target
        target_group = pygame.sprite.Group()
        for target in range(3):
            new_target = Target()
            target_group.add(new_target)

        score = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:  # shoot
                    # gun_sound.play()
                    hits = pygame.sprite.spritecollide(player, target_group, True)
                    for hit in hits:
                        score = score + 1
                        new_target = Target()
                        target_group.add(new_target)

            wn.blit(bg_img, (0, 0))

            target_group.update()
            target_group.draw(wn)

            player_group.update()
            player_group.draw(wn)

            score_board(score)

            pygame.display.flip()
            clock.tick(60)

    # pygame quit
    game_loop()
    pygame.quit()
    quit()


def game1():
    # General setup
    pygame.init()

    clock = pygame.time.Clock()

    # color
    BLACK = (0, 0, 0)

    # Game window
    wn_width = 600
    wn_height = 500
    wn = pygame.display.set_mode((wn_width, wn_height))
    pygame.display.set_caption('Shoot asteroids')
    programIcon = pygame.image.load('images/icon.ico')
    pygame.display.set_icon(programIcon)

    # images and sounds
    bg_img = pygame.image.load('images/background.jpg')
    bg_img = pygame.transform.scale(bg_img, (600, 600))
    target_img = pygame.image.load('images/asteroid2.png')
    target_img2 = pygame.image.load('images/asteroid 1.png')
    crosshair_img = pygame.image.load('images/crosshair.png')
    # gun_sound = pygame.mixer.Sound('sounds/laser_sound.wav')
    pygame.mouse.set_visible(False)

    # Database sqLite3

    conn = sqlite3.connect("Score.db")
    c = conn.cursor()

    c.execute(
        '''CREATE TABLE IF NOT EXISTS block(
            score int

        )'''
    )
    conn.commit()
    conn.close()

    def score_board(score):
        global usernam1
        font = pygame.font.Font('freesansbold.ttf', 35)
        text = font.render('Score ' + str(score), True, (255, 255, 255))
        wn.blit(text, (5, 10))

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = crosshair_img
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.center = pygame.mouse.get_pos()

    class Target(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            ran_no = random.randint(1, 2)
            if ran_no == 1:
                self.image = target_img
            else:
                self.image = target_img2
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, wn_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randrange(1, 2)
            self.speedx = random.randrange(-1, 2)

        def update(self):
            global score, usernam1
            self.rect.x = self.rect.x + self.speedx
            self.rect.y = self.rect.y + self.speedy

            if self.rect.right < 0 or self.rect.left > wn_width:
                self.rect.x = random.randint(0, wn_width - self.rect.width)
                self.rect.y = random.randint(-100, -40)
                self.speedy = random.randint(1, 4)
                self.speedx = random.randint(-1, 2)

            if self.rect.top > wn_height:  # game over
                font = pygame.font.Font(None, 80)
                text = font.render('Game Over', True, BLACK)
                wn.blit(text, (150, 150))
                pygame.display.flip()
                time.sleep(2)

                db = sqlite3.connect("Score.db")
                c = db.cursor()
                c.execute(
                    f'''SELECT * FROM user_score WHERE :usernam={ent.get}'''
                )
                d = c.fetchall()
                e = d[0]
                e_0 = e[0]
                e_1 = e[1]
                e_2 = e[2]
                c.execute(f''' DElETE FROM user_score WHERE :usernam={usernam1}''')
                db.commit()
                if score > e_1:
                    e_1 = score

                c.execute(
                    'INSERT INTO user_score VALUES (:usernam,:score, :password)',
                    {
                        "usernam": e_0,
                        "score": e_1,
                        "password": e_2

                    },

                )
                db.commit()

    def game_loop():
        # Player
        player = Player()
        player_group = pygame.sprite.Group()
        player_group.add(player)

        # Target
        target_group = pygame.sprite.Group()
        for target in range(3):
            new_target = Target()
            target_group.add(new_target)

        score = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:  # shoot
                    # gun_sound.play()
                    hits = pygame.sprite.spritecollide(player, target_group, True)
                    for hit in hits:
                        score = score + 1
                        new_target = Target()
                        target_group.add(new_target)

            wn.blit(bg_img, (0, 0))

            target_group.update()
            target_group.draw(wn)

            player_group.update()
            player_group.draw(wn)

            score_board(score)

            pygame.display.flip()
            clock.tick(60)

    # pygame quit
    game_loop()
    pygame.quit()
    quit()

def mode_sel():
    """ function to select the game mode for users"""
    global  mode_bgimg, mode_boximg,easy_img, hard_img
    mode_fr = LabelFrame(root).place(x=0, y=0)

    # placement of bg
    mode_bgimg = PhotoImage(file='images/bg.PNG')
    bg_img = Label(mode_fr, image=mode_bgimg, bg='#FFBF3B', bd=0)
    bg_img.place(x=0, y=0)

    # box image place
    mode_boximg = PhotoImage(file='images/box.PNG')
    box_img = Label(mode_fr, image=mode_boximg, bg='#FFBC35', bd=0)
    box_img.place(x=199, y=164)

    # button placement
    easy_img=PhotoImage(file='images/EasyBtn.png')
    but = Button(mode_fr, command=game1, image=easy_img, bg='#030303', bd=0,
                 activebackground="Black").place(x=294,
                                                 y=204)
    hard_img=PhotoImage(file='images/Hardbtn.png')
    but2 = Button(mode_fr, command=game1, image=hard_img, bg='#030303', bd=0,
                 activebackground="Black").place(x=294,
                                                 y=300)
def signup():
    global bgimg, en_img, psw_img, bt_img, boximg

    signup_fr = LabelFrame(root).place(x=0, y=0)

    # Background image entry
    bgimg = PhotoImage(file='images/bg.PNG')
    bg_img = Label(signup_fr, image=bgimg, bg='#FFBF3B', bd=0)
    bg_img.place(x=0, y=0)

    # box image place
    boximg = PhotoImage(file='images/box.PNG')
    box_img = Label(signup_fr, image=boximg, bg='#FFBC35', bd=0)
    box_img.place(x=179, y=108)

    def clear_entry(events):
        """ remove placeholder after selection"""

        if usernam.get() == "Username":
            usernam.set("")

    def clear_pw(events):
        """ remove placeholder after selection"""

        if password.get() == "Password":
            password.set("")
    # username entry
    en_img = PhotoImage(file='images/entry.png')
    ent_img = Label(signup_fr, image=en_img, bg='#030303', fg="#FFBF3B", bd=0)
    ent_img.place(x=240, y=131)

    usernam = StringVar()
    usernam.set('Username')
    ent = Entry(signup_fr, text=usernam, bg='#FFBF3B', fg="#030303", bd=0, font=("Arial", 15))
    ent.place(x=250, y=141)
    ent.bind("<Button-1>", clear_entry)

    # password entry

    psw_img = PhotoImage(file='images/entry.png')
    pw_img = Label(signup_fr, image=psw_img, bg='#030303', fg="#030303", bd=0, font=("Arial", 15))
    pw_img.place(x=240, y=220)

    password = StringVar()
    password.set('Password')
    pw_ent = Entry(signup_fr, text=password, bg='#FFBF3B', fg="#030303", bd=0, font=("Ribeye", 15))
    pw_ent.place(x=250, y=230)
    pw_ent.bind("<Button-1>", clear_pw)

    bt_img = PhotoImage(file='images/done.png')

    def done_click():

        """ Creates a table to store the user credentials and score after sign up"""
        global username

        #datbase and creating cursor
        user_info = sqlite3.connect("Score.db")
        c = user_info.cursor()

        #creating table
        c.execute(
            '''CREATE TABLE IF NOT EXISTS user_score(
            usernam text,
            score integer,
            password integer

            )'''
        )
        user_info.commit()

        # storing values in the table
        c.execute(
            'INSERT INTO user_score VALUES (:usernam,:score, :password)',
            {
                "usernam": usernam.get(),
                "score": 0,
                "password": password.get()

            },

        )
        user_info.commit()

    # button to confirm the entered data
    but = Button(signup_fr, text='confirm', command=done_click, image=bt_img, bg='#030303', bd=0,
                 activebackground="Black").place(x=289,
                                                 y=279)


def login():

    """ Starting page of the game which allows user to play or create new account"""

    global bgimg, en_img, psw_img, bt_img, bt_img2, usernam1


    login_fr = LabelFrame(root).place(x=0, y=0)

    # background image
    bgimg = PhotoImage(file='images/bg.png')
    bg_img = Label(login_fr, image=bgimg)
    bg_img.place(x=0, y=0)

    def play_click():
        """ Check username and password, and allows user to enter the game if credentials are correct"""


        user_info = sqlite3.connect("Score.db")
        c = user_info.cursor()

        c.execute(
            '''SELECT * FROM user_score '''
        )
        d = c.fetchall()
        e = len(d)
        valid1 = False
        valid2 = False
        for i in range(0, e):
            g = d[i]
            if usernam1.get() == g[0]:
                valid1 = True
                if password1.get() == g[2]:
                    valid2 = True

        if valid1 is False:
            message='Invaid Username'

        elif valid1 is True and valid2 is False:
            message="Invalid Passsword"

        else:
            message=" "
            mode_sel()
        mess_box=Label(login_fr, text=message, font=('Ariel',15), bg="black", fg="#FFBF3B").place(x=316, y=375)


    # box image place
    boximg = PhotoImage(file='images/rectanglelogin.PNG')
    box_img = Label(login_fr, image=boximg, bg='#030303', bd=0)
    box_img.place(x=179, y=108)

    # username entry
    en_img = PhotoImage(file='images/loginentry.png')
    ent_img = Label(login_fr, image=en_img, bg='#030303', bd=0)
    ent_img.place(x=240, y=131)

    def clear_entry(events):
        """ remove placeholder after selection"""

        if usernam1.get() == "Username":
            usernam1.set("")

    def clear_pw(events):
        """ remove placeholder after selection"""

        if password.get() == "Password":
            password.set("")

    def vari():
        global usernam1, usernam1_1
        usernam1_1 = usernam1

    usernam1 = StringVar()
    usernam1.set('Username')
    ent = Entry(login_fr, text=usernam1, bg='#FFBF3B', fg="#030303", bd=0, font=("Arial", 15))
    ent.place(x=260, y=147)
    ent.bind("<Button-1>", clear_entry)

    # password entry
    psw_img = PhotoImage(file='images/loginentry.png')
    pw_img = Label(login_fr, image=psw_img, bg='#030303', bd=0)
    pw_img.place(x=240, y=220)

    password1 = StringVar()
    password1.set('Password')
    pw_ent = Entry(login_fr, text=password1, bg='#FFBF3B', fg="#030303", bd=0, font=("Arial", 15))
    pw_ent.place(x=250, y=230)
    pw_ent.bind("<Button-1>", clear_entry)

    bt_img = PhotoImage(file='images/play.png')
    but = Button(login_fr, command=play_click, image=bt_img, bg='#000000', bd=0, activebackground="Black").place(x=294,
                                                                                                                 y=309)

    bt_img2 = PhotoImage(file='images/Signup.png')
    but2 = Button(login_fr, command=signup, image=bt_img2, bg='#000000', bd=0, activebackground="Black").place(x=480,
                                                                                                               y=378)

    vari()


login()

root.mainloop()
