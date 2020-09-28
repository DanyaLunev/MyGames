from pygame import *

antivirus_w = 20
antivirus_h = 20


class Antivirus(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((antivirus_w, antivirus_h))
        self.image = image.load("textures/Антивирус.png")
        self.rect = Rect(x, y, antivirus_w, antivirus_h)