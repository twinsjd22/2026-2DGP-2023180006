from pico2d import *

SCREEN_WIDTH = 1200             # 화면 너비
SCREEN_HEIGHT = 800             # 화면 높이
SCALE = 10                      # 확대 배율
CENTER_X = SCREEN_WIDTH // 2    # 화면 가운데 x
GROUND_Y = 150                  # 소닉 발이 닿는 높이
FRAME_DELAY = 0.1               # 프레임 사이 간격(초)

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)

sonic = load_image('sonic-sprite.png')

# 프레임 좌표: (left, bottom, width, height)

# 1번 줄: 대기
idle_frames = [
    (1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 29, 39), (87, 447, 29, 38),
    (118, 447, 30, 38), (150, 447, 30, 38), (182, 447, 30, 38), (212, 448, 28, 38),
    (240, 448, 29, 38), (270, 448, 24, 32), (302, 448, 29, 26),
]

left, bottom, width, height = idle_frames[0]
clear_canvas()
sonic.clip_draw(left, bottom, width, height, CENTER_X, SCREEN_HEIGHT // 2, width * SCALE, height * SCALE)
update_canvas()
delay(2)

close_canvas()
