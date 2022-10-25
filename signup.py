from plane_sprites import *

BLANK_IMAGE = "images/blank.png"



class SignUp(GameSprite):

    def __init__(self):
        super().__init__(BLANK_IMAGE)

        # self.image = pygame.image.load(BLANK_IMAGE)
        self.image = pygame.transform.scale(self.image,(70, 50))
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_RECT.centerx + 70
        self.rect.top = SCREEN_RECT.centery + self.rect.height * 4
        self.click = False
        self.hit = "Sign up"
        self.exist = False
        self.success = False
    