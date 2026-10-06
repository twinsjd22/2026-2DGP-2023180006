from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
FRAME_SIZE = 100   # 스프라이트 한 칸의 크기
MOVE_SPEED = 10    # 한 프레임에 움직이는 거리(px)
FRAME_DELAY = 0.05

# animation_sheet.png에서 동작별 줄의 bottom 좌표
IDLE_RIGHT, IDLE_LEFT, RUN_RIGHT, RUN_LEFT = 300, 200, 100, 0

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    """방향키를 누르면 방향을 더하고, 떼면 되돌린다. 창 닫기와 ESC는 종료."""
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


def update_boy():
    """좌우로 움직일 때만 바라보는 방향을 바꾸고, 화면 안에서만 이동한다."""
    global x, y, face_dir

    if dir_x != 0:
        face_dir = dir_x
    x += dir_x * MOVE_SPEED
    y += dir_y * MOVE_SPEED
    x = clamp(FRAME_SIZE // 2, x, TUK_WIDTH - FRAME_SIZE // 2)
    y = clamp(FRAME_SIZE // 2, y, TUK_HEIGHT - FRAME_SIZE // 2)


def draw_boy():
    """움직이면 달리기, 멈추면 대기 줄을 바라보는 방향에 맞춰 그린다."""
    if dir_x != 0 or dir_y != 0:
        action = RUN_RIGHT if face_dir == 1 else RUN_LEFT
    else:
        action = IDLE_RIGHT if face_dir == 1 else IDLE_LEFT
    character.clip_draw(frame * FRAME_SIZE, action, FRAME_SIZE, FRAME_SIZE, x, y)


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x, dir_y = 0, 0
face_dir = 1  # 1: 오른쪽, -1: 왼쪽

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_boy()
    update_canvas()
    handle_events()
    update_boy()
    frame = (frame + 1) % 8
    delay(FRAME_DELAY)

close_canvas()
