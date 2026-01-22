from os.path import join
from pyray import *
from raylib import *




init_window(1920, 1080, "Base")

# import images/textures
cowboy_image = load_image("../assets/animation/0.png")
image_color_invert(cowboy_image)
cowboy_texture = load_texture_from_image(cowboy_image)


spaceship_texture = load_texture("../assets/spaceship.png")  # for some reason you have to manuever and find the spaceship???
spaceship_image = load_image("../assets/spaceship.png")
image_color_grayscale(spaceship_image)
new_texture = load_texture_from_image(spaceship_image)



# import font 
font = load_font("../assets/Zero Hour.otf") 






while not window_should_close():
    begin_drawing()
    clear_background(BLACK)

    # custom shape drawing
    draw_pixel(100, 200, RED)
    draw_pixel_v(Vector2(200, 200), WHITE)
    draw_circle(500, 100, 100, GREEN)
    draw_circle_v(Vector2(1000, 600), 200, YELLOW)
    draw_line_ex(Vector2(0, 0), Vector2(500, 200), 10, RED)

    # YOUTUBE TIME STAMP 35:05 https://www.youtube.com/watch?v=UoAsDlUwjy0

    # display images
    draw_texture(spaceship_texture, 0, 0, WHITE)
    draw_texture_v(new_texture, Vector2(100, 0), WHITE)
    draw_texture(cowboy_texture, 1800, 900, WHITE)




    # displaying text
    draw_text("Some text", 0, 400, 100, WHITE)
    draw_text_ex(font, 'Some more text', Vector2(0,600), 20, 0, BLUE)

    end_drawing()

close_window()
