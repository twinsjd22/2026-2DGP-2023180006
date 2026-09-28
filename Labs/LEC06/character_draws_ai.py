from pico2d import *
import math

CENTER_X, CENTER_Y = 400, 300
RADIUS = 200


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    print('circle')
    for degree in range(0, 360, 2):
        theta = math.radians(degree)
        x = CENTER_X + RADIUS * math.cos(theta)
        y = CENTER_Y + RADIUS * math.sin(theta)
        draw_character(x, y)


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
