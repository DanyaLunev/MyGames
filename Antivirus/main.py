from player import *
from platform import *
from item import *
from levels import *
from antivirus import *
import time
from start import *
from pygame import *

WIDTH = 600
HEIGHT = 600
window = (WIDTH, HEIGHT)
COLOR = '#363636'
COUNTER = 0
TIMER = 0


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIDTH / 2, -t + HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width - WIDTH), l)
    t = max(-(camera.height - HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)


def main():
    all_sprite = sprite.Group()
    platform = []
    item = []
    antivirus = []

    left = right = False
    up = False

    hero = Player(55, 55)
    all_sprite.add(hero)

    init()

    timer = time.Clock()

    screen = display.set_mode(window)
    display.set_caption('Антивирус')
    bg = Surface(window)
    bg.fill(Color(COLOR))
    close = False

    back = image.load("textures/фон-1.png")

    start = BottomS(200, 200)
    startF = False
    screen.blit(back, (0, 0))
    screen.blit(start.image, (200, 200))
    Exit = BottomE(200, 300)
    screen.blit(Exit.image, (200, 300))
    display.update()

    while not startF:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                pos = mouse.get_pos()

                if (pos[0] > 200 and pos[0] < 400) and (pos[1] > 200 and pos[1] < 250):
                    startF = True

                    img = image.load("textures/Кат.сцена.png")
                    screen.blit(img, (0, 0))
                    display.update()
                    time.wait(2500)
                    all_sprite.remove(img)

                    img2 = image.load("textures/Кат.сцена2.png")
                    screen.blit(img2, (0, 0))
                    display.update()
                    time.wait(2500)
                    all_sprite.remove(img2)

                    img3 = image.load("textures/Кат.сцена3.png")
                    screen.blit(img3, (0, 0))
                    display.update()
                    time.wait(2500)
                    all_sprite.remove(img3)

                    img4 = image.load("textures/Кат.сцена4.png")
                    screen.blit(img4, (0, 0))
                    display.update()
                    time.wait(2500)
                    all_sprite.remove(img4)

                if (pos[0] > 200 and pos[0] < 400) and (pos[1] > 300 and pos[1] < 350):
                    quit()

    if GLOBAL_COUNTER == 0:
        win = YouWin(200, 200)
        winF = False
        screen.blit(back, (0, 0))
        screen.blit(win.image, (200, 200))
        display.update()

        while not winF:
            for b in event.get():
                if b.type == MOUSEBUTTONDOWN:
                    pos = mouse.get_pos()

                    if (pos[0] > 200 and pos[0] < 400) and (pos[1] > 200 and pos[1] < 250):
                        quit()

    x = y = 0
    total_camera_w = len(level[0]) * platform_w
    total_camera_h = len(level) * platform_h
    camera = Camera(camera_configure, total_camera_w, total_camera_h)

    for rl in level:
        for cl in rl:
            if cl == "-":
                pl = Platform(x, y)
                all_sprite.add(pl)
                platform.append(pl)

            if cl == "*":
                it = Item(x, y)
                all_sprite.add(it)
                item.append(it)

            if cl == "+":
                ant = Antivirus(x, y)
                all_sprite.add(ant)
                antivirus.append(ant)

            x += platform_w
        y += platform_h
        x = 0

    while not close:
        timer.tick(60)

        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    left = True

                if e.key == K_RIGHT:
                    right = True

                if e.key == K_UP:
                    up = True

            if e.type == KEYUP:
                if e.key == K_LEFT:
                    left = False

                if e.key == K_RIGHT:
                    right = False

                if e.key == K_UP:
                    up = False

            if e.type == QUIT:
                close = True

        screen.blit(bg, (0, 0))

        COUNTER = hero.update(left, right, up, platform, item, antivirus)
        camera.update(hero)

        for i in all_sprite:
            screen.blit(i.image, camera.apply(i))
        hero.draw_text(screen, str(COUNTER), 50)
        display.update()

    quit()


if __name__ == '__main__':
    main()
