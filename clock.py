#  usage: python3 ./clock.py "20:50:00"

import sys
import time
from datetime import datetime, timedelta
import os
import shutil

os.system('clear')
print('\n' * int(shutil.get_terminal_size().lines / 2))

initTime = sys.argv[1:][0]

hour, minutes, seconds = initTime.split(':')

curTime = datetime.now()
changedTime = curTime.replace(hour=int(hour), minute=int(minutes), second=int(seconds))

diff = changedTime - curTime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

warnTimeLow = curTime.replace(hour=int(20), minute=int(4), second=int(0))
warnTimeLow2 = curTime.replace(hour=int(20), minute=int(5), second=int(40))
warnTimeTop = curTime.replace(hour=int(20), minute=int(5), second=int(50))

critTimeLow = curTime.replace(hour=int(20), minute=int(5), second=int(50))
critTimeTop = curTime.replace(hour=int(20), minute=int(6), second=int(5))

try:
	while True:
		newTime = datetime.now() + diff
		color = bcolors.OKGREEN

		if warnTimeLow <  newTime < warnTimeTop:
			color = bcolors.WARNING
			if warnTimeLow2 < newTime < warnTimeTop:
				if int(newTime.strftime("%Y%m%d%H%M%S")) % 2:
					color = bcolors.BOLD
		elif critTimeLow < newTime < critTimeTop:
			if int(newTime.strftime("%Y%m%d%H%M%S")) % 2:
				color = bcolors.BOLD
			else:
				color = bcolors.FAIL

		timeStr = newTime.strftime('\t{}%H:%M:%S{}'.format(color, bcolors.ENDC))
		print(timeStr.center(shutil.get_terminal_size().columns), end='\r')
		sys.stdout.flush()
		time.sleep(1)
except KeyboardInterrupt:
    # User interrupt the program with ctrl+c
	print()
	exit()
