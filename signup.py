from plane_sprites import *

BLANK_IMAGE = "images/blank.png"



class SignUp(GameSprite):

    def __init__(self):
        super().__init__(BLANK_IMAGE)

        self.image = pygame.image.load(BLANK_IMAGE)
        self.image = pygame.transform.scale(self.image,(300, 50))
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_RECT.centerx - self.rect.width / 2
        self.rect.top = SCREEN_RECT.centery + self.rect.height * 4
        self.click = False
    