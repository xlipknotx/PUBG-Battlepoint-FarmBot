from getch import pause
from colorama import *
import os
from FarmBot import Bot
import webbrowser
import sys
import shutil
import subprocess
from time import sleep
import coords
from psutil import process_iter
import threading

def clear():
    """
    Clears the console screen using the built in commands on a operating
    system (here linux and windows)
    """
    os.system(['clear', 'cls', "^L"][os.name == 'nt'])
init()
verde = Fore.GREEN + Style.BRIGHT
bot = Bot()
pause("""This is a try to get the bot stop crash,
just press enter and it will be displayed the 4 configs 
that the gui has""")
print(verde + '''
1- 1920x1080
2- 2560x1440
3- 1366x768 (720)
4- 1680x1050''')
abc = input("Your resolution is... : ")
while True:
	if abc is "1":
		bot.setConfig('1080')
		break
		clear()
	if abc is "2":
		bot.setConfig('1440')
		break
		clear()
	if abc is "3":
		bot.setConfig('720')
		break
		clear()
	if abc is "4":
		bot.setConfig('w1440')
		break
		clear()
	else:
		print('you didn´t select one of the previous')
		clear()
print("""You have selected your resolution,
if you press enter the bot is going to start""")
pause(" ")
def start_bot():
	thr = threading.Thread(target=bot.run)
	thr.start()
start_bot()

