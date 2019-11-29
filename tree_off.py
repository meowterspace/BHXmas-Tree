import board
import neopixel
import psutil
import os


def tree_off():
	for proc in psutil.process_iter():
		pinfo = proc.as_dict(attrs=['pid', 'name'])
		procname = str(pinfo['name'])
		procpid = str(pinfo['pid'])
		if "python" in procname and procpid != str(os.getpid()):
			print("Killing process", proc)
			proc.kill()

	pixels = neopixel.NeoPixel(board.D18, 300)
	pixels.fill((0,0,0))

if __name__ == '__main__':
	tree_off()
