from email.mime import image
from plane_sprites import*
import random

SMALL_ENEMY_IMAGE = "images/enemy1.png"
MID_ENEMY_IMAGE = "images/enemy2.png"
LARGE_ENEMY_IMAGE = "images/enemy3.png"
ENEMY_SPEED_MIN = 1
ENEMY_SPEED_MAX = 5

class MidEnemy(GameSprite):
    life = 5

    def __init__(self):
        super().__init__(MID_ENEMY_IMAGE)

        self.destory_images = []
        self.destory_images.extend([\
            pygame.image.load("images/enemy2_down.png"),\
            pygame.image.load("images/enemy2_down2.png"),\
            pygame.image.load("images/enemy2_down3.png"),\
            pygame.image.load("images/enemy2_down4.png")\
            ])
        self.image_hit = pygame.image.load("images/enemy2_hit.png")
        self.speed = 2
        self.life = MidEnemy.life
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.y = -200
        self.die = False


    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("delete successfully")
        pass

class SmallEnemy(GameSprite):
    life = 1 

    def __init__(self):
        super().__init__(SMALL_ENEMY_IMAGE)

        self.destory_images = []
        self.destory_images.extend([\
            pygame.image.load("images/enemy1_down.png"),\
            pygame.image.load("images/enemy1_down2.png"),\
            pygame.image.load("images/enemy1_down3.png"),\
            pygame.image.load("images/enemy1_down4.png")\
            ])
        self.speed = 2
        self.life = SmallEnemy.life
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.y = -50
        self.die = False


    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("delete successfully")
        pass

class  LargeEnemy(GameSprite):
    life = 20
    def __init__(self):
        super().__init__(LARGE_ENEMY_IMAGE)

        self.destory_images = []
        self.destory_images.extend([\
            pygame.image.load("images/enemy3_down.png"),\
            pygame.image.load("images/enemy3_down2.png"),\
            pygame.image.load("images/enemy3_down3.png"),\
            pygame.image.load("images/enemy3_down4.png"),\
            pygame.image.load("images/enemy3_down5.png"),\
            pygame.image.load("images/enemy3_down6.png")\
            ])
        self.image_hit = pygame.image.load("images/enemy3_hit.png")
        self.speed = 2
        self.life = LargeEnemy.life
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.y = -300
        self.die = False


    def update(self):
        super().update()
        
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("delete successfully")
        pass