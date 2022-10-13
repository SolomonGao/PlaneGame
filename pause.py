from turtle import width
from plane_sprites import *

PAUSE_IMAGE = "images/pause.png"
PAUSE_PRESSED_IMAGE =  "images/pause_hover.png"
RESUME_IMAGE = "images/resume.png"
RESUME_PRESSED_IMAGE = "images/resume.png"


class Pause(GameSprite):

    def __init__(self):
        super().__init__(PAUSE_IMAGE)

        self.pause = pygame.image.load(PAUSE_IMAGE)
        self.pause_pressed = pygame.image.load(PAUSE_PRESSED_IMAGE)
        self.resume = pygame.image.load(RESUME_IMAGE)
        self.resume_pressed = pygame.image.load(RESUME_PRESSED_IMAGE)

        self.paused = False
        self.rect = self.pause_pressed.get_rect()
        self.rect.left = SCREEN_RECT.right - self.rect.width
        self.rect.top = SCREEN_RECT.top + 10
        
        

