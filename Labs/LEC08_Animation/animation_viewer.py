from pico2d import *

open_canvas()

kirby = load_image('kirby.png')

def draw_walk():
    print("걷기")
    pass

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
    clear_canvas()
    kirby.clip_draw(10, 454, 27, 26, 400, 300)
    draw_walk()
    draw_run()
    draw_jump()
    draw_attack()
    update_canvas()

close_canvas()