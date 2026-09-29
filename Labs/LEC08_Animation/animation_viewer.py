from pico2d import *

open_canvas()

kirby = load_image('kirby.png')

walk_frames = [
    (125, 454, 35, 28), (165, 456, 35, 28), (207, 457, 32, 27), (246, 457, 29, 26),
    (285, 457, 26, 27), (320, 457, 26, 28), (355, 457, 26, 27), (390, 457, 26, 27),
    (426, 457, 26, 28), (461, 457, 26, 26), (496, 457, 28, 26), (532, 457, 30, 26),
]

run_frames = [
    (130, 414, 36, 28), (171, 414, 32, 28), (210, 414, 30, 28), (247, 414, 30, 27),
    (286, 414, 31, 27), (324, 414, 30, 27), (362, 414, 30, 28), (399, 414, 32, 28),
]

jump_frames = [
    (131, 373, 30, 29), (170, 375, 27, 33), (207, 377, 28, 28), (243, 375, 26, 23),
    (280, 374, 23, 27), (315, 372, 26, 30), (350, 368, 28, 31), (388, 372, 25, 40),
    (421, 372, 27, 39), (461, 373, 23, 35), (498, 372, 24, 25), (537, 372, 26, 23),
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
    delay(1)

def draw_run():
    for i in range(5):
        for left, bottom, width, height in run_frames:
            clear_canvas()
            kirby.clip_draw(left, bottom, width, height,
                            400, 230 + height * 5 // 2,
                            width * 5, height * 5)
            update_canvas()
            delay(0.1)
    delay(1)

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