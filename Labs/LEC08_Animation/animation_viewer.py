from pico2d import *

SCALE = 8           # 확대 배율
CENTER_X = 400      # 화면 가운데 x
GROUND_Y = 180      # 커비 발이 닿는 높이
FRAME_DELAY = 0.1   # 프레임 사이 간격(초)
REPEAT_COUNT = 5    # 한 동작 반복 횟수
PAUSE_TIME = 1      # 동작이 끝난 뒤 정지 시간(초)

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

attack_frames = [
    (280, 53, 33, 33), (321, 53, 30, 30), (360, 53, 30, 33), (422, 53, 32, 34),
    (463, 53, 42, 40), (515, 53, 23, 44), (549, 53, 24, 37),
]

def play_animation(frames):
    for i in range(REPEAT_COUNT):
        for left, bottom, width, height in frames:
            clear_canvas()
            kirby.clip_draw(left, bottom, width, height,
                            CENTER_X, GROUND_Y + height * SCALE // 2,
                            width * SCALE, height * SCALE)
            update_canvas()
            delay(FRAME_DELAY)
    delay(PAUSE_TIME)

def draw_walk():
    play_animation(walk_frames)

def draw_run():
    play_animation(run_frames)

def draw_jump():
    play_animation(jump_frames)

def draw_attack():
    play_animation(attack_frames)

while True:
    draw_walk()
    draw_run()
    draw_jump()
    draw_attack()

close_canvas()