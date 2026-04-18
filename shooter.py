#Создай собственный Шутер!

from pygame import *

window = display.set_mode((500, 500))
bg = transform.scale(image.load('galaxy.jpg'), (500, 500))
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(bg, (0, 0))
    display.update()
