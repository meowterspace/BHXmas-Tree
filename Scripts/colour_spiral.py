import time
import board
import neopixel
import random
import json
import os
from Utils import tree_colours, tree_utils

path = os.path.dirname(os.path.abspath(__file__))
with open(path+'/Config/config.json') as config_data:
    config = json.load(config_data)

cols = tree_colours.basic_colors

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

for x in range(dead_pixels):
    pixels[x] = (0, 0, 0)

def fade_looper():
    col = cols[random.randint(0, len(cols)-1)]
    col = tree_utils.hex_to_rgb(col)
    for i in range(dead_pixels, num_pixels):
         print(i)
         for j in range(dead_pixels, num_pixels):
             if (i == j):
                 pixels[j] = col
             pix = list(map(lambda x: x - 1 if x -1 > 0 else 0, list(pixels[j])))
             pixels[j] = (pix[0], pix[1], pix[2])
         pixels.show()

    col = cols[random.randint(0, len(cols)-1)]
    col = tree_utils.hex_to_rgb(col)
    for i in range(num_pixels, dead_pixels, -1):
         print(i)
         for j in range(dead_pixels, num_pixels):
             if (i == j):
                 pixels[j] = col
             pix = list(map(lambda x: x - 1 if x -1 > 0 else 0, list(pixels[j])))
             pixels[j] = (pix[0], pix[1], pix[2])
         pixels.show()

def looper():
    col = cols[random.randint(0, len(cols)-1)]
    for i in range(dead_pixels, num_pixels):
        pixels[i] = tree_utils.hex_to_rgb(col)
        print(pixels[i])
        pixels.show()
    col = cols[random.randint(0, len(cols)-1)]
    for i in range(1, num_pixels-dead_pixels):
        pixels[num_pixels-i] = tree_utils.hex_to_rgb(col)
        pixels.show()

while True:
#    looper()
    fade_looper()
