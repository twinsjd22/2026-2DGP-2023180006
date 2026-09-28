# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')
def draw_boy(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_line(x0, y0, x1, y1):
    n = 100
    for step in range(n + 1):
        t = step / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_boy(x, y)

def draw_top():
    print("top")
    for x in range(50, 751, 5):
        draw_boy(x, 550)

def draw_right():
    print("right")
    for y in range(550, 49, -5):
        draw_boy(750, y)

def draw_bottom():
    print("bottom")
    for x in range(750, 49, -5):
        draw_boy(x, 50)

def draw_left():
    print("left")
    for y in range(50, 551, 5):
        draw_boy(50, y)

def draw_ab():
    print("ab")
    for x in range(100, 701, 5):
        draw_boy(x, 100)

def draw_bc():
    print("bc")
    move_line(700, 100, 400, 500)

def draw_ca():
    print("ca")
    n = 100
    for step in range(n + 1):
        t = step / n
        x = 400 + (100 - 400) * t
        y = 500 + (100 - 500) * t
        draw_boy(x, y)

def move_circle():
    print('circle')
    for degree in range(0, 360, 2):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_boy(x, y)

def move_rectangle():
    print('rectangle')
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    
def move_triangle():
    print('triangle')
    draw_ab()
    draw_bc()
    draw_ca()

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()