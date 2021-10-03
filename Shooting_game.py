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

    global bgimg, psw_img,bt_img, bt_img2
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
    ent.place(x=240, y=131)

    #password entry
    psw_img = PhotoImage(file='images/loginentry.png')
    pw_img = Label(login_fr, image=psw_img, bg='#030303', bd=0)
    pw_img.place(x=240, y=220)

    password=StringVar()
    pw_ent=Entry(login_fr, text=password,bg='#FFBF3B',fg="#030303", bd=0, font=("Arial", 15))
    pw_ent.place(x=250,y=230)

    def signup():
        global bgimg, en_img, psw_img, bt_img, boximg

        signup_fr = LabelFrame(root).place(x=0, y=0)

        # Background image entry
        bgimg = PhotoImage(file='images/bg.PNG')
        bg_img = Label(signup_fr, image=bgimg, bg='#FFBF3B', bd=0)
        bg_img.place(x=0, y=0)

        # box image place
        boximg = PhotoImage(file='images/box.PNG')
        box_img = Label(signup_fr, image=boximg, bg='#030303', bd=0)
        box_img.place(x=179, y=108)

        # username entry
        en_img = PhotoImage(file='images/entry.png')
        ent_img = Label(signup_fr, image=en_img, bg='#030303', fg="#FFBF3B", bd=0)
        ent_img.place(x=240, y=131)

        username = StringVar()
        username.set('Username')
        ent = Entry(signup_fr, text=username, bg='#FFBF3B', fg="#030303", bd=0, font=("Arial", 15))
        ent.place(x=250, y=141)

        # password entry

        psw_img = PhotoImage(file='images/entry.png')
        pw_img = Label(signup_fr, image=psw_img, bg='#030303', fg="#030303", bd=0, font=("Arial", 15))
        pw_img.place(x=240, y=220)

        password = StringVar()
        password.set('Password')
        pw_ent = Entry(signup_fr, text=password, bg='#FFBF3B', fg="#030303", bd=0, font=("Arial", 15))
        pw_ent.place(x=250, y=230)

        bt_img = PhotoImage(file='images/done.png')

        def done_click():
            global username
            user_info = sqlite3.connect("Score.db")
            c = user_info.cursor()
            c.execute(
                '''CREATE TABLE IF NOT EXISTS user_score(
                username text,
                score integer,
                password integer,

                )'''
            )
            c.commit()

            c.execute(
                '''INSERT INTO user_score VALUES (:username,:score, :password)''',
                {
                    "username": username.get(),
                    "score": 0,
                    "password": password.get(),

                },

            )
            c.commit()

        but = Button(signup_fr, text='confirm', command=done_click, image=bt_img, bg='#030303', bd=0).place(x=289,
                                                                                                            y=279)

    def game():
        # General setup
        pygame.init()

        clock = pygame.time.Clock()

        # color
        BLACK = (0, 0, 0)

        # Game window
        wn_width = 600
        wn_height = 500
        wn = pygame.display.set_mode((wn_width, wn_height))
        pygame.display.set_caption('Kill CoronaVirus')

        # images and sounds
        bg_img = pygame.image.load('images/background.png')
        bg_img = pygame.transform.scale(bg_img, (600, 600))
        target_img = pygame.image.load('images/asteroid2.png')
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
                self.image = target_img
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(0, wn_width - self.rect.width)
                self.rect.y = random.randint(-100, -40)
                self.speedy = random.randrange(1, 4)
                self.speedx = random.randrange(-1, 2)

            def update(self):
                global score
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
                        '''INSERT INTO user_score VALUES (:username,:score)''',
                        {
                            "username": username.get(),
                            "score": score,

                        },

                    )
                    c.commit()

                    game_loop()

        def game_loop():
            # Player
            player = Player()
            player_group = pygame.sprite.Group()
            player_group.add(player)

            # Target
            target_group = pygame.sprite.Group()
            for target in range(6):
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

    bt_img = PhotoImage(file='images/play.png')
    but = Button(login_fr, command=signup(), image=bt_img, bg='#000000',bd=0).place(x=294, y=309)

    bt_img2 = PhotoImage(file='images/Signup.png')
    but2 = Button(login_fr, command=login(), image=bt_img2, bg='#000000',bd=0).place(x=480, y=378)




login()

root.mainloop()