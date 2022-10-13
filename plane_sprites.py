import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)

FRAME_RATE = 60
# eventid, Add one event by using USEREVENT + 1
CREATE_SMALL_ENEMY_EVENT = pygame.USEREVENT
CREATE_MID_ENEMY_EVENT = pygame.USEREVENT + 1
CREATE_LARGE_ENEMY_EVENT = pygame.USEREVENT + 2
HERO_FIRE_EVENT = pygame.USEREVENT + 3
RELOAD_BOMB_EVENT = pygame.USEREVENT + 4

BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):

        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speed