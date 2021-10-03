import pygame
import random
import time
import sqlite3
from tkinter import *

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
    bg_img = pygame.image.load('images/background2.jpg')
    bg_img = pygame.transform.scale(bg_img, (600, 600))
    target_img = pygame.image.load('images/basteroid2.png')
    target_img2 = pygame.image.load('images/basteroid1.png')
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
            ran_no=random.randint(1,2)
            if ran_no==1 :
                self.image = target_img
            else:
                self.image=target_img2
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, wn_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randrange(2, 4)
            self.speedx = random.randrange(-1, 4)

        def update(self):
            global score
            self.rect.x = self.rect.x + self.speedx
            self.rect.y = self.rect.y + self.speedy

            if self.rect.right < 0 or self.rect.left > wn_width:
                self.rect.x = random.randint(0, wn_width - self.rect.width)
                self.rect.y = random.randint(-100, -40)
                self.speedy = random.randint(2, 4)
                self.speedx = random.randint(-1, 4)

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

game()