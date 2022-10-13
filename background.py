from plane_sprites import *

IMAGE_NAME = "images/background.png"

class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__(IMAGE_NAME)

        if is_alt:
            self.rect.y = - SCREEN_RECT.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
