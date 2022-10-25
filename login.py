from plane_sprites import *

BLANK_IMAGE = "images/blank.png"



class LogIn(GameSprite):

    def __init__(self):
        super().__init__(BLANK_IMAGE)

        self.image = pygame.image.load(BLANK_IMAGE)

        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_RECT.centerx - self.rect.width / 2
        self.rect.top = SCREEN_RECT.centery + self.rect.height * 4
        self.click = False