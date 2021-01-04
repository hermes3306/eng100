import datetime;
import os;
from time import sleep;

def typefile(fname):
	f = open(fname)
	while True:
		l = f.readline()
		if not l: break
		print(l)
		sleep(1)
	f.close()

start = datetime.datetime(2020, 12, 5, 0, 0, 0)
while True:
	now = datetime.datetime.now()
	day = now - start 
	fname = "" + str(day.days) + ".txt"
	typefile("/home/pi/code/eng100/" + fname);
	print("*")
	sleep(3)
	os.system('clear')
