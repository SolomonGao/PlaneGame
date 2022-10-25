from plane_sprites import *

RESTART_IMAGE = "images/restart.jpg"



class Restart(GameSprite):

    def __init__(self):
        super().__init__(RESTART_IMAGE)

        self.restart = pygame.image.load(RESTART_IMAGE)

        self.doesrestart = False
        self.rect = self.restart.get_rect()
        self.rect.left = SCREEN_RECT.centerx - self.rect.width / 2
        self.rect.top = SCREEN_RECT.centery + self.rect.height