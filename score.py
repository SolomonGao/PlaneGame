from plane_sprites import *


class Score(GameSprite):

    def __init__(self):
        self.position = (0, 10)

        self.score = 0
        self.font =  pygame.font.SysFont('arial',28)

    
    def update(self):
        pass
