from pico2d import *

SCREEN_WIDTH = 1200             # 화면 너비
SCREEN_HEIGHT = 800             # 화면 높이
SCALE = 10                      # 확대 배율
CENTER_X = SCREEN_WIDTH // 2    # 화면 가운데 x
GROUND_Y = 150                  # 소닉 발이 닿는 높이
FRAME_DELAY = 0.1               # 프레임 사이 간격(초)
PLAY_TIME = 5                   # 한 동작 재생 시간(초)
PAUSE_TIME = 1                  # 동작이 끝난 뒤 정지 시간(초)

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)

sonic = load_image('sonic-sprite.png')

# 프레임 좌표: (left, bottom, width, height)

# 1번 줄: 대기
idle_frames = [
    (1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 29, 39), (87, 447, 29, 38),
    (118, 447, 30, 38), (150, 447, 30, 38), (182, 447, 30, 38), (212, 448, 28, 38),
    (240, 448, 29, 38), (270, 448, 24, 32), (302, 448, 29, 26),
]

# 2번 줄: 걷기
walk_frames = [
    (8, 408, 26, 37), (37, 408, 27, 37), (65, 407, 31, 38), (97, 408, 37, 37),
    (135, 410, 32, 35), (170, 408, 32, 38), (206, 408, 26, 38), (238, 408, 24, 37),
    (263, 408, 30, 37), (295, 408, 36, 37), (334, 409, 32, 36), (370, 408, 29, 38),
]

# 3번 줄: 달리기
run_frames = [
    (1, 361, 33, 40), (39, 362, 35, 39), (89, 362, 35, 38), (130, 362, 34, 42),
    (181, 362, 34, 41), (228, 363, 33, 40),
]

# 4번 줄: 스핀(몸을 말기)
spin_frames = [
    (1, 326, 29, 30), (35, 327, 29, 31), (67, 327, 30, 29), (98, 327, 31, 29),
    (131, 327, 29, 30), (162, 326, 29, 31), (193, 326, 30, 29), (230, 326, 31, 29),
    (268, 325, 30, 30),
]

# 5번 줄: 볼(구르기)
ball_frames = [
    (1, 292, 30, 27), (36, 292, 29, 27), (70, 292, 29, 27), (105, 292, 29, 27),
    (139, 292, 29, 27), (174, 292, 29, 27),
]

# 6번 줄: 가속
dash_frames = [
    (1, 251, 29, 35), (36, 251, 30, 35), (74, 251, 31, 35), (111, 251, 31, 36),
    (149, 251, 30, 35), (186, 251, 31, 36),
]

# 7번 줄: 피겨에이트 달리기
peel_out_frames = [
    (1, 207, 29, 35), (36, 207, 30, 35), (72, 208, 39, 31), (123, 208, 39, 32),
    (172, 208, 39, 31), (218, 208, 38, 32),
]

def play_animation(frames):
    start_time = get_time()
    frame = 0
    while get_time() - start_time < PLAY_TIME:
        left, bottom, width, height = frames[frame]
        clear_canvas()
        sonic.clip_draw(left, bottom, width, height,
                        CENTER_X, GROUND_Y + height * SCALE // 2,
                        width * SCALE, height * SCALE)
        update_canvas()
        frame = (frame + 1) % len(frames)
        delay(FRAME_DELAY)
    delay(PAUSE_TIME)

play_animation(idle_frames)
play_animation(walk_frames)
play_animation(run_frames)
play_animation(spin_frames)
play_animation(ball_frames)
play_animation(dash_frames)
play_animation(peel_out_frames)

close_canvas()
