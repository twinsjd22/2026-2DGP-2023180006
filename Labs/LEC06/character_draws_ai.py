from pico2d import *


def move_circle():
    print('circle')


def move_rectangle():
    print('rectangle')


def move_triangle():
    print('triangle')


open_canvas(800, 600)
character = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
