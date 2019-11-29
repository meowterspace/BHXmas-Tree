import os
import subprocess
import time
import signal
import json

path = os.path.dirname(os.path.abspath(__file__))

with open(path+'/Scripts/Config/patterns.json') as patterns_data:
	patterns = json.load(patterns_data)

files = os.listdir('Scripts')

files = list(filter(lambda x: x.endswith('.py'), files))

print('Christmas Tree Activated')
print ('Iterating through:')
print (files)
print ('and ' + str(len(patterns)) + ' colour patterns')

def run_prog(duration, filepath, args = ''):
	pro = subprocess.Popen(['sudo', 'python3', filepath, args])
	time.sleep(duration)

	pid = pro.pid
	for y in range(pid, pid+10):
		try:
		        os.kill(y, signal.SIGTERM)
		except:
			pass

while True:
	for file in files:
		print(file)
		run_prog(60, 'Scripts/'+file)
	for index in range(0, len(patterns)):
		print(index)
		run_prog(30, 'Scripts/Utils/multicolour.py', str(index))
