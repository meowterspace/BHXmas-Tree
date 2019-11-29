import time
import board
import neopixel
import math 
import json
import os
import sys
import tree_utils

path = os.path.dirname(os.path.abspath(__file__))
with open(path+'/../Config/config.json') as config_data:
    config = json.load(config_data)
with open(path+'/../Config/patterns.json') as patterns_data:
    patterns = json.load(patterns_data)

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

index = sys.argv[1]
pattern = patterns[int(index)]

def looper():
    length = len(pattern)
    s = (length*10)-1
    for j in range(s):
        for i in range(dead_pixels, num_pixels):
            y = int(((i - j) % 10) * 25.5)
            k = int((i - j)/10) % length
            r, g, b = (0, 0, 0)
            for l in range(length):
                if k == l:
                    col = tree_utils.hex_to_rgb(pattern[l])
            pixels[i] = col
        pixels.show()
        time.sleep(0.1)
 
 
while True:
    looper()
