from plane_sprites import *

RESTART_IMAGE = "images/restart.png"



class Restart(GameSprite):

    def __init__(self):
        super().__init__(RESTART_IMAGE)

        # self.image = pygame.image.load(RESTART_IMAGE)
        self.image = pygame.transform.scale(self.image,(300, 50))
        self.doesrestart = False
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_RECT.centerx - self.rect.width / 2
        self.rect.top = SCREEN_RECT.centery + self.rect.height