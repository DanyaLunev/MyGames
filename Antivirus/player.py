from pygame import *

speed = 7
widthP = 35
heightP = 35
gravity = 0.35
jump = 8
GLOBAL_COUNTER = 3


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.onGround = False
        self.speedX = 0
        self.speedY = 0
        self.startX = x
        self.startY = y
        self.image = Surface((widthP, heightP))
        self.image = image.load("textures/Игрок.png")
        self.rect = Rect(x, y, widthP, heightP)
        self.count = 3
        self.anti = 0

    def update(self, left, right, up, platforms, items, antivirus):
        if up:
            if self.onGround:
                self.speedY -= jump

        if left:
            self.speedX = -speed

        if right:
            self.speedX = speed

        if not (left or right):
            self.speedX = 0

        if not self.onGround:
            self.speedY += gravity

        self.onGround = False

        self.rect.x += self.speedX

        self.collide(self.speedX, 0, platforms, items, antivirus, self.anti, GLOBAL_COUNTER)

        self.rect.y += self.speedY

        self.collide(0, self.speedY, platforms, items, antivirus, self.anti, GLOBAL_COUNTER)

        return self.count

    def collide(self, speedX, speedY, platforms, items, antivirus, anti, GLOBAL_COUNTER):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if speedX > 0:
                    self.rect.right = p.rect.left

                if speedX < 0:
                    self.rect.left = p.rect.right

                if speedY > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.speedY = 0

                if speedY < 0:
                    self.rect.top = p.rect.bottom
                    self.speedY = 0

        for a in antivirus:
            if sprite.collide_rect(self, a):
                a.kill()
                antivirus.remove(a)
                self.anti += 1

        for i in items:
            if anti == 1:
                if sprite.collide_rect(self, i):
                    i.kill()
                    items.remove(i)
                    self.count -= 1
                    GLOBAL_COUNTER = self.count

    def draw_text(self, surf, text, size):
        x = 550
        y = 5

        font1 = font.Font(None, 50)

        text_p = font1.render("Вирусов :", True, (0, 0, 0))
        text_r = Rect(x - 170, y, 100, size)
        surf.blit(text_p, text_r)

        text_s = font1.render(text, True, (0, 0, 0))
        text_r = Rect(x, y, 100, size)
        surf.blit(text_s, text_r)