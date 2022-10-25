from plane_sprites import *
from bullet import *
import pygame


HERO_IMAGE = "images/me.png"
HERO_IMAGE2 = "images/me1.png"


class Hero(GameSprite):

    def __init__(self):
        super().__init__(HERO_IMAGE, 3)
        
        self.image2 = pygame.image.load(HERO_IMAGE2)
        self.destory_images = []
        self.destory_images.extend([\
            pygame.image.load("images/me_destory1.png"),\
            pygame.image.load("images/me_destory2.png"),\
            pygame.image.load("images/me_destory3.png"),\
            pygame.image.load("images/me_destory4.png")\
            ])
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.die = False
        self.bullet_group = pygame.sprite.Group()
        self.bomb_num = 3
        self.fire_sound = pygame.mixer.Sound("sounds/bullet.wav")
        self.fire_sound.set_volume(0.2)
        self.bomb_sound = pygame.mixer.Sound("sounds/fire.wav")
        self.bomb_sound.set_volume(0.4)
        self.stop = False
                    




    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.right - self.rect.width:
            self.rect.x = SCREEN_RECT.right - self.rect.width
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_RECT.bottom - self.rect.height:
            self.rect.y = SCREEN_RECT.bottom - self.rect.height

    def fire(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            self.fire_sound.play()
            bullet = Bullet1()

            bullet.rect.bottom = self.rect.y
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)

    def bomb(self):
            self.bomb_sound.play()
            bullet = Bullet2()
            bullet.rect.bottom = self.rect.y
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)
            
            self.bomb_num -= 1

            
            
            

    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed


    def reset(self):
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.die = False
        self.stop = False
        self.bomb_num = 3

        
