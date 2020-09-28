from pygame import *

platform_w = 50
platform_h = 50


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_w, platform_h))
        self.image = image.load("textures/Блок.png")
        self.rect = Rect(x, y, platform_w, platform_h)


class Platform2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_w, platform_h))
        self.image = image.load("textures/Блок.png")
        self.rect = Rect(x, y, platform_w, platform_h)


class Platform3(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_w, platform_h))
        self.image = image.load("textures/Блок.png")
        self.rect = Rect(x, y, platform_w, platform_h)