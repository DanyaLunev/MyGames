from pygame import *

width_bot = 200
heigth_bot = 50


class BottomS(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((width_bot, heigth_bot))
        self.image = image.load("textures/Старт.png")
        self.rect = Rect(x, y, width_bot, heigth_bot)


class BottomE(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((width_bot, heigth_bot))
        self.image = image.load("textures/Выход.png")
        self.rect = Rect(x, y, width_bot, heigth_bot)


class YouWin(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((width_bot, heigth_bot))
        self.image = image.load("textures/Win.png")
        self.rect = Rect(x, y, width_bot, heigth_bot)