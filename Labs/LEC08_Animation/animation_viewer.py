from pico2d import *

open_canvas()

kirby = load_image('kirby.png')

def draw_walk():
    clear_canvas()
    kirby.clip_draw(125, 454, 35, 28, 400, 300)
    update_canvas()

def draw_run():
    print("뛰기")
    pass

def draw_jump():
    print("점프")
    pass

def draw_attack():
    print("공격")
    pass

while True:
    draw_walk()
    draw_run()
    draw_jump()
    draw_attack()

close_canvas()