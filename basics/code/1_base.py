from pyray import *
from raylib import *

init_window(1920, 1080, "Base")


while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_pixel(100, 200, RED)
    draw_pixel_v(Vector2(200, 200), WHITE)

    draw_circle(500, 100, 100, GREEN)
    draw_circle_v(Vector2(1000, 600), 200, YELLOW)

    draw_line_ex(Vector2(0, 0), Vector2(500, 200), 10, RED)

    # YOUTUBE TIME STAMP 20:19

    end_drawing()

close_window()
