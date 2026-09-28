# 실습 과제 진행
from pico2d import *
from math import *
# 맨처음 해야할 일은.
open_canvas(800, 600)
character = load_image('character.png')

degree = 0
theta = math.radians(degree)
x = 400 + 200 * math.cos(theta)
y = 300 + 200 * math.sin(theta)

def move_circle():
    global degree, x, y
    print('circle')
    degree += 0.02
    theta = math.radians(degree)
    x = 400 + 200 * math.cos(theta)
    y = 300 + 200 * math.sin(theta)
    # 캐릭터 이미지 표시
    clear_canvas()
    character.draw(x, y)
    update_canvas()

def move_rectangle():
    print('rectangle')
    pass
def move_triangle():
    print('triangle')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()