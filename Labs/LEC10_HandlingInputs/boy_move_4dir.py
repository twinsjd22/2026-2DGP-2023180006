from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
FRAME_SIZE = 100
MOVE_SPEED = 10
FRAME_DELAY = 0.05

# animation_sheet.png에서 동작별 줄의 bottom 좌표
IDLE_RIGHT, IDLE_LEFT, RUN_RIGHT, RUN_LEFT = 300, 200, 100, 0

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * FRAME_SIZE, IDLE_RIGHT, FRAME_SIZE, FRAME_SIZE, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(FRAME_DELAY)

close_canvas()
