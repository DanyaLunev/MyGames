from pygame import *

item_w = 25
item_h = 25
item_color = '#e32417'


class Item(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((item_w, item_h))
        self.image = image.load("textures/Вирус.png")
        self.rect = Rect(x, y, item_w, item_h)