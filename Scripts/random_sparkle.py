import random
import time
import board
import neopixel
import json
import os
from Utils import tree_colours, tree_utils

path = os.path.dirname(os.path.abspath(__file__))
with open(path+'/Config/config.json') as config_data:
    config = json.load(config_data)

safe = tree_colours.safe_colors

num_pixels = config['num_pixels']
dead_pixels = config['dead_pixels']

# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D18

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

while True:
    pixel = random.randrange(dead_pixels, num_pixels)
    col = tree_utils.hex_to_rgb(safe[random.randint(0, len(safe)-1)])

    pixels[pixel] = col
    pixels.show()
