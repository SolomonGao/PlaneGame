from telnetlib import GA
from plane_sprites import GameSprite

BULLET_IMAGE = "images/bullet1.png"
SUPER_BULLET_IMAGE = "images/bomb.png"

class Bullet1(GameSprite):
    damage = 1

    def __init__(self):
        super().__init__(BULLET_IMAGE, -10)

        self.damage = Bullet1.damage

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("Delete bullet")
        pass

class Bullet2(GameSprite):
    damage = 4

    def __init__(self):
        super().__init__(SUPER_BULLET_IMAGE, -8)
        self.damage = Bullet2.damage

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("Delete bullet")
        pass