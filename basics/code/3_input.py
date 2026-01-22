from pyray import *
from raylib import * 
from os.path import join




init_window(1920, 1080, "Input")
set_exit_key(KEY_ESCAPE) # closes the while loop and ends the game. 




ship_texture = load_texture("../assets/spaceship.png")
ship_pos = Vector2(0,0)
ship_direction = Vector2(0,0)
ship_speed = 800

while not window_should_close():
    # input 
    # mouse input 
    # ship_pos = get_mouse_position() 
   
    
    # if is_mouse_button_pressed(0):
    #     print('mouse button pressed') 
    
  
    # ship and keyboard input 
    ship_direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))   # int is converting the value of true and false 1=true 0=false 
    ship_direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))      # remember this pattern for movement!!!!!!!!!!! 
    ship_direction = Vector2Normalize(ship_direction) 
    
    
    # update 
    dt = get_frame_time() 
    ship_pos.x += ship_direction.x * ship_speed * dt 
    ship_pos.y += ship_direction.y * ship_speed * dt 
    
    
    
    
    
    
    
    
    
    
    
    # drawing 
    begin_drawing()
    clear_background(BLACK)
    draw_texture_v(ship_texture, ship_pos, WHITE)
    end_drawing()
close_window()