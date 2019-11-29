import time
import board
import neopixel
import math

# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D18

# On a Raspberry pi, use this instead, not all pins are supported
#pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 300

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)


a = (68,97,118)
b = (105,100,32)
c = (83,109,101)
d = (108,108,115)

while True:
	for i in range(len(pixels)):
		if i%4==0: pixels[i] = d
		elif i%3==0: pixels[i] = c
		elif i%2==0: pixels[i] = b
		else: pixels[i] = a
	pixels.show()
