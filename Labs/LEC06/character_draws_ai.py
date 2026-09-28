from pico2d import *
import math

CENTER_X, CENTER_Y = 400, 300
RADIUS = 200
STEP = 5  # 한 프레임에 이동하는 거리(픽셀)

RECTANGLE = [(50, 550), (750, 550), (750, 50), (50, 50)]


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_line(x0, y0, x1, y1):
    n = max(1, int(math.hypot(x1 - x0, y1 - y0) / STEP))
    for i in range(n + 1):
        t = i / n
        draw_character(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)


def move_polygon(points):
    for i in range(len(points)):
        x0, y0 = points[i]
        x1, y1 = points[(i + 1) % len(points)]
        move_line(x0, y0, x1, y1)


def move_circle():
    print('circle')
    for degree in range(0, 360, 2):
        theta = math.radians(degree)
        x = CENTER_X + RADIUS * math.cos(theta)
        y = CENTER_Y + RADIUS * math.sin(theta)
        draw_character(x, y)


def move_rectangle():
    print('rectangle')
    move_polygon(RECTANGLE)


def move_triangle():
    print('triangle')


open_canvas(800, 600)
character = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
