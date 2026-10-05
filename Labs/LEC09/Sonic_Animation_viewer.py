# Sonic 애니메이션 뷰어: 스프라이트시트의 모든 동작을 5초씩 재생하고 1초 쉬며 무한 반복한다.
from pico2d import *

SCREEN_WIDTH = 1200             # 화면 너비
SCREEN_HEIGHT = 800             # 화면 높이
SCALE = 12                      # 확대 배율 (가장 큰 프레임 45px → 540px)
CENTER_X = SCREEN_WIDTH // 2    # 화면 가운데 x
GROUND_Y = 120                  # 소닉 발이 닿는 높이
FRAME_DELAY = 0.1               # 프레임 사이 간격(초)
PLAY_TIME = 5                   # 한 동작 재생 시간(초)
PAUSE_TIME = 1                  # 동작이 끝난 뒤 정지 시간(초)

# 가로 이동 속도(px/초): 양수는 오른쪽, 음수는 왼쪽
WALK_SPEED = 150
RUN_SPEED = 400
ROLL_SPEED = 500
DASH_SPEED = 300
PEEL_OUT_SPEED = 700
HURT_SPEED = -200               # 피격되면 뒤로 밀려남
START_OFFSET = 200              # 이동 동작이 출발하는 가장자리로부터의 거리
EDGE_MARGIN = 300               # 화면 밖 여유 폭 (가장 넓은 프레임 480px의 절반보다 크게)

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

# 8번 줄 앞: 제자리 회전
turn_frames = [
    (1, 154, 24, 45), (31, 154, 29, 44), (65, 154, 20, 44), (90, 155, 25, 43),
    (119, 155, 25, 43), (149, 154, 20, 44),
]

# 8번 줄 뒤: 피격
hurt_frames = [
    (184, 156, 40, 28), (232, 157, 39, 27),
]

# 9번 줄: 정면 달리기
front_run_frames = [
    (1, 108, 27, 38), (31, 110, 31, 36), (64, 110, 31, 36), (99, 110, 33, 38),
    (136, 110, 32, 36), (176, 110, 33, 36), (217, 110, 33, 36), (254, 111, 33, 36),
]

# 10번 줄 앞: 놀람
surprise_frames = [
    (6, 56, 34, 40), (49, 56, 34, 43),
]

# 10번 줄 뒤: 포즈
pose_frames = [
    (96, 59, 23, 39), (125, 59, 23, 39),
]

# 재생 순서: (프레임 리스트, 가로 이동 속도)
animations = [
    (idle_frames, 0),
    (walk_frames, WALK_SPEED),
    (run_frames, RUN_SPEED),
    (spin_frames, 0),
    (ball_frames, ROLL_SPEED),
    (dash_frames, DASH_SPEED),
    (peel_out_frames, PEEL_OUT_SPEED),
    (turn_frames, 0),
    (hurt_frames, HURT_SPEED),
    (front_run_frames, 0),          # 화면 쪽으로 달려서 가로 이동 없음
    (surprise_frames, 0),
    (pose_frames, 0),
]

# 창 닫기, ESC 키가 들어오면 종료 표시
def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 이벤트를 받으면서 seconds초 동안 기다린다
def wait(seconds):
    start_time = get_time()
    while running and get_time() - start_time < seconds:
        handle_events()
        delay(0.01)

# 제자리 동작은 가운데, 오른쪽 이동은 왼쪽 가장자리, 왼쪽 이동은 오른쪽 가장자리에서 출발
def get_start_x(speed):
    if speed > 0:
        return START_OFFSET
    if speed < 0:
        return SCREEN_WIDTH - START_OFFSET
    return CENTER_X

# 한 동작을 PLAY_TIME초 동안 반복 재생하고 PAUSE_TIME초 정지
# speed만큼 경과 시간에 비례해 가로로 이동한다
# 발이 GROUND_Y에 닿도록 프레임 높이의 절반만큼 올려서 그린다
def play_animation(frames, speed):
    start_x = get_start_x(speed)
    start_time = get_time()
    frame = 0
    while running and get_time() - start_time < PLAY_TIME:
        x = start_x + speed * (get_time() - start_time)
        x = (x + EDGE_MARGIN) % (SCREEN_WIDTH + 2 * EDGE_MARGIN) - EDGE_MARGIN    # 화면 밖으로 나가면 반대편에서 등장
        left, bottom, width, height = frames[frame]
        clear_canvas()
        sonic.clip_draw(left, bottom, width, height,
                        x, GROUND_Y + height * SCALE // 2,
                        width * SCALE, height * SCALE)
        update_canvas()
        frame = (frame + 1) % len(frames)
        wait(FRAME_DELAY)
    wait(PAUSE_TIME)

# 전체 동작을 무한 반복 (종료 시 play_animation이 바로 돌아옴)
running = True
while running:
    for frames, speed in animations:
        play_animation(frames, speed)

close_canvas()
