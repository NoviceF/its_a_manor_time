#  usage: python3 ./clock.py "20:50:00"

import sys
import time
from datetime import datetime, timedelta

initTime = sys.argv[1:][0]

hour, minutes, seconds = initTime.split(':')

curTime = datetime.now()
curTime = curTime.replace(hour=int(hour), minute=int(minutes), second=int(seconds))

oneSec = timedelta(seconds=1)

newTime = curTime

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

try:
	while True:
		print(newTime.strftime('\t{}%H:%M:%S{}'.format(bcolors.OKGREEN, bcolors.ENDC)), end='\r')
		newTime = newTime + oneSec
		sys.stdout.flush()
		time.sleep(1)
except KeyboardInterrupt:
    # User interrupt the program with ctrl+c
	print()
	exit()
