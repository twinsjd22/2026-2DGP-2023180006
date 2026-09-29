from pico2d import *

open_canvas()

kirby = load_image('kirby.png')

walk_frames = [
    (125, 454, 35, 28), (165, 456, 35, 28), (207, 457, 32, 27), (246, 457, 29, 26),
    (285, 457, 26, 27), (320, 457, 26, 28), (355, 457, 26, 27), (390, 457, 26, 27),
    (426, 457, 26, 28), (461, 457, 26, 26), (496, 457, 28, 26), (532, 457, 30, 26),
]

def draw_walk():
    for i in range(5):
        for left, bottom, width, height in walk_frames:
            clear_canvas()
            kirby.clip_draw(left, bottom, width, height,
                            400, 230 + height * 5 // 2,
                            width * 5, height * 5)
            update_canvas()
            delay(0.1)

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