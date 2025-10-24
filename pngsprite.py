"""PNG sprite helper.

Provides a small wrapper around the PNG decoder to extract and draw
individual frames from a spritesheet PNG.

Classes:
    PNGSprite(display, png_file, width, height)
"""
from pngdec import PNG # type: ignore

class PNGSprite:
    """Load and draw sprites from a PNG spritesheet.

    Parameters:
        display: Display object (e.g. PicoGraphics) used for drawing.
        png_file (str): Path to the spritesheet PNG file.
        width (int): Width of a single sprite frame in pixels.
        height (int): Height of a single sprite frame in pixels.
    """
    def __init__(self, display, png_file, width, height):
        self.png_file = png_file
        self.width = width
        self.height = height
        self.display = display
        
    def get_sprite(self, sx, sy, dx, dy, scale=1):
        """Draw a single sprite frame from the spritesheet.

        Parameters:
            sx (int): Source sprite X index (column) in the spritesheet.
            sy (int): Source sprite Y index (row) in the spritesheet.
            dx (int): Destination X coordinate on the display to draw the sprite.
            dy (int): Destination Y coordinate on the display to draw the sprite.
            scale (int | float, optional): Scale factor to apply when drawing.
                                            Defaults to 1 (no scaling).

        Behaviour:
            Opens the PNG file, decodes the rectangular region corresponding to
            the sprite at (sx, sy) and blits it to (dx, dy) on the provided
            display with the given scale.
        """
        png = PNG(self.display)
        png.open_file(self.png_file)
        png.decode(dx, dy, scale, source=(sx * self.width, sy * self.height, self.width, self.height))