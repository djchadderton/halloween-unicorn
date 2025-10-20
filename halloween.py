from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN
from utime import sleep
from pngsprite import PNGSprite
from sequences import ghosts, bats, pumpkin, pumpkin2

gu = GalacticUnicorn()
display = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN)

WIDTH = GalacticUnicorn.WIDTH
HEIGHT = GalacticUnicorn.HEIGHT

BLACK = display.create_pen(0, 0, 0)
SKY = display.create_pen(20, 13, 237)
RED = display.create_pen(96, 0, 0)
YELLOW = display.create_pen(127, 80, 0)

ghost_sprites = PNGSprite(display, "pacman_ghosts.png", 11, 11)
bat_sprite = PNGSprite(display, "bat3.png", 31, 13)
pumpkin_sprite = PNGSprite(display, "pumpkins.png", 13, 11) 

def clear_to_colour(colour):
    display.set_pen(colour)
    display.clear()
    gu.update(display)

def fadeColor(startR, startG, startB, endR, endG, endB, steps):
    for i in range(steps):
        r = startR + (endR - startR) * i // steps
        g = startG + (endG - startG) * i // steps
        b = startB + (endB - startB) * i // steps
        clear_to_colour(display.create_pen(r, g, b))
        sleep(0.1) # Adjust delay for speed

def play_sequence(sequence, spritesheet, background):
    for frame in sequence:
        display.set_pen(background)
        display.clear()
        for sprite in frame["frame"]:
            scale = frame["scale"] if "scale" in frame else 1
            
            spritesheet.get_sprite(*sprite, scale)
        
        gu.update(display)
        sleep(frame["pause"])

# Init
text = "Happy Hallowe'en"
win_x = 14
win_y = 4
win_width = 41
scale = 0.4
display.set_font("serif")
msg_width = display.measure_text(text, scale)

while True:
    # Pacman ghosts
    play_sequence(ghosts, ghost_sprites, BLACK)

    # Bat flight
    fadeColor(0, 0, 0, 20, 13, 237, 10)
    play_sequence(bats, bat_sprite, SKY)
    clear_to_colour(BLACK)
    sleep(1)

    # Pumpkin
    display.set_clip(0, 0, 13, 11)
    play_sequence(pumpkin, pumpkin_sprite, BLACK)

    # Text
    display.set_pen(RED)
    display.set_thickness(1)

    display.set_clip(14, 0, win_width, 11)

    for z in range (msg_width + win_width + 2):
        x = win_x - z + win_width
        y = win_y
        
        clear_to_colour(BLACK)
        display.set_pen(YELLOW)
        
        display.text(text, x - 1, y - 1, -1, scale)
        display.text(text, x, y - 1, -1, scale)
        display.text(text, x + 1, y - 1, -1, scale)
        display.text(text, x - 1, y, -1, scale)
        display.text(text, x + 1, y, -1, scale)
        display.text(text, x - 1, y + 1, -1, scale)
        display.text(text, x, y + 1, -1, scale)
        display.text(text, x + 1, y + 1, -1, scale)

        display.set_pen(RED)
        display.text(text, x, y, -1, scale)
        gu.update(display)
        sleep(0.1)

    display.remove_clip()

    play_sequence(pumpkin2, pumpkin_sprite, BLACK)
    clear_to_colour(BLACK)
    sleep(1)
