from pico2d import *

open_canvas(1280, 1024)
tuk_ground = load_image('TUK_GROUND.png')

clear_canvas()
tuk_ground.draw(1280 // 2, 1024 // 2)
update_canvas()
delay(2)

close_canvas()
