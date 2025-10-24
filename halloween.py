"""Halloween Unicorn demo

This module runs a simple Halloween-themed animation on a Galactic Unicorn
display using sprites and sequences.

Top-level behaviour:
- Animates ghost, bat and pumpkin sprite sequences.
- Performs background colour fades.
- Shows scrolling text with a shadow.

Note: This file is intended to run on a Pico/Galactic Unicorn environment.

Functions:
    clear_to_colour(colour)
    fadeColor(startR, startG, startB, endR, endG, endB, steps, delay=0.1)
    play_sequence(sequence, spritesheet, background)
"""
from galactic import GalacticUnicorn # type: ignore
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN # type: ignore
from utime import sleep # type: ignore
from pngsprite import PNGSprite
from sequences import ghosts, bats, pumpkin, pumpkin2

gu = GalacticUnicorn()
display = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN)

WIDTH = GalacticUnicorn.WIDTH
HEIGHT = GalacticUnicorn.HEIGHT

# Define colours
BLACK = display.create_pen(0, 0, 0)
SKY = display.create_pen(20, 13, 237)
RED = display.create_pen(96, 0, 0)
YELLOW = display.create_pen(127, 80, 0)

# Initiate spritesheets
ghost_sprites = PNGSprite(display, "pacman_ghosts.png", 11, 11)
bat_sprite = PNGSprite(display, "bat3.png", 31, 13)
pumpkin_sprite = PNGSprite(display, "pumpkins.png", 13, 11) 

def clear_to_colour(colour):
    """Clear the display to a single colour and update the hardware.

    Parameters:
        colour: pen handle returned by display.create_pen(...) representing the
                RGB colour to clear the screen to.

    Effects:
        - Sets the display pen to `colour`.
        - Clears the display buffer.
        - Calls gu.update(display) to push the buffer to the screen.
    """
    display.set_pen(colour)
    display.clear()
    gu.update(display)

def fadeColor(startR, startG, startB, endR, endG, endB, steps, delay = 0.1):
    """Fade the display background colour from a start RGB to an end RGB.

    Parameters:
        startR, startG, startB: integers (0-255) for the starting RGB colour.
        endR, endG, endB: integers (0-255) for the ending RGB colour.
        steps: number of intermediate steps in the fade (integer > 0).
        delay: seconds to sleep between steps (float, default 0.1).

    Behaviour:
        Calculates linearly interpolated RGB values per step, clears the
        display to each intermediate colour, updates the hardware and sleeps
        for `delay` seconds between frames.
    """
    for i in range(steps):
        r = startR + (endR - startR) * i // steps
        g = startG + (endG - startG) * i // steps
        b = startB + (endB - startB) * i // steps
        clear_to_colour(display.create_pen(r, g, b))
        sleep(delay)

def play_sequence(sequence, spritesheet, background):
    """Play a sequence of sprite frames on the display.

    Parameters:
        sequence: iterable of frames where each frame is a dict. Expected keys:
            - "frame": list/iterable of sprite descriptors (arguments passed to
                       spritesheet.get_sprite).
            - "pause": seconds to sleep after drawing the frame.
            - optional "scale": scale factor to pass to get_sprite for this frame.
        spritesheet: PNGSprite instance used to draw sprites.
        background: pen handle for the background colour (from display.create_pen).

    Behaviour:
        For each frame in `sequence`:
        - Clears the display to `background`.
        - Draws every sprite described in frame["frame"] using spritesheet.get_sprite.
        - Calls gu.update(display) and sleeps for frame["pause"] seconds.
    """
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

# Main loop
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

    # Set clipping region for text animation
    display.set_clip(14, 0, win_width, 11)

    for z in range (msg_width + win_width + 2):
        x = win_x - z + win_width
        y = win_y
        
        clear_to_colour(BLACK)

        # Draw shadow
        display.set_pen(YELLOW)
        
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                display.text(text, x + dx, y + dy, -1, scale)

        # Draw text
        display.set_pen(RED)
        display.text(text, x, y, -1, scale)
        gu.update(display)
        sleep(0.1)

    display.remove_clip()

    play_sequence(pumpkin2, pumpkin_sprite, BLACK)
    clear_to_colour(BLACK)
    sleep(1)
