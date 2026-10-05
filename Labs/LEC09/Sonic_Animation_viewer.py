from pico2d import *

open_canvas(1200, 800)

sonic = load_image('sonic-sprite.png')

clear_canvas()
sonic.draw(600, 400)
update_canvas()
delay(2)

close_canvas()
