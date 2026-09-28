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
    
def draw_top():
    print("top")
    for x in range(50, 751, 5):
        draw_boy(x, 550)
    pass
def draw_right():
    print("right")
    for y in range(550, 49, -5):
        draw_boy(750, y)
    pass
def draw_bottom():
    print("bottom")
    for x in range(750, 49, -5):
        draw_boy(x, 50)
    pass
def draw_left():
    print("left")
    for y in range(50, 551, 5):
        draw_boy(50, y)
    pass

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
    pass
def move_triangle():
    print('triangle')
    pass

while True:
    #move_circle()
    move_rectangle()
    move_triangle()

close_canvas()