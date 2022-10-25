from plane_sprites import *

SHOW_SCORE_IMAGE = "images/highscore.jpg"



class HighScore(GameSprite):

    def __init__(self):
        super().__init__(SHOW_SCORE_IMAGE)

        self.restart = pygame.image.load(SHOW_SCORE_IMAGE)

        self.show = False
        self.rect = self.restart.get_rect()
        self.rect.left = SCREEN_RECT.centerx - self.rect.width / 2
        self.rect.top = SCREEN_RECT.centery + self.rect.height * 3