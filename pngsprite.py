from pngdec import PNG

class PNGSprite:
    def __init__(self, display, png_file, width, height):
        self.png_file = png_file
        self.width = width
        self.height = height
        self.display = display
        
    def get_sprite(self, sx, sy, dx, dy, scale=1):
        png = PNG(self.display)
        png.open_file(self.png_file)
        png.decode(dx, dy, scale, source=(sx * self.width, sy * self.height, self.width, self.height))