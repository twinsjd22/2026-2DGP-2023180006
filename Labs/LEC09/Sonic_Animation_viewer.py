from pico2d import *

SCREEN_WIDTH = 1200             # 화면 너비
SCREEN_HEIGHT = 800             # 화면 높이
SCALE = 10                      # 확대 배율
CENTER_X = SCREEN_WIDTH // 2    # 화면 가운데 x
GROUND_Y = 150                  # 소닉 발이 닿는 높이
FRAME_DELAY = 0.1               # 프레임 사이 간격(초)

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)

sonic = load_image('sonic-sprite.png')

clear_canvas()
sonic.draw(CENTER_X, SCREEN_HEIGHT // 2)
update_canvas()
delay(2)

close_canvas()
