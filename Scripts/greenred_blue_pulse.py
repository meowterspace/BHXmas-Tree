import time
import board
import neopixel
import math 
import os
import json

path = os.path.dirname(os.path.abspath(__file__))
with open(path+'/Config/config.json') as config_data:
    config = json.load(config_data)

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
 

def looper(n, p):
    for j in range(n, p):
        jj = j
        if j > (p/2):
            jj = p - j
        for i in range(dead_pixels, num_pixels):
            y = int(((i - j) % 10) * 25.5)
            r = int((i/300)*y)
            g = int(((300-i)/300)*y)
            c = 0
            if (j > 0):
                c = int(jj)*4
            col = (g, r, c)
            pixels[i] = col
        pixels.show()
        time.sleep(0.1)

while True:
    looper(-10, 40)
