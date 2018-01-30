import requests as re
from getch import pause
from bs4 import BeautifulSoup
from colorama import Fore, init, Style
init()
color = Fore.GREEN + Style.BRIGHT
target = 'https://pubgafkfarmerversion.000webhostapp.com/'
texto = re.get(target)
soup = BeautifulSoup(texto.text, 'html5lib')
version = soup.title.string
float(version)
file = open('version.txt' , 'r', encoding='utf-8')
archivo = file.readlines()
version_actual = archivo[0]
if (version == version_actual):
	print(color + "You are up to date")
else:
	print(Fore.RED + Style.BRIGHT+ """You have to update it, 
check https://github.com/peleon02/PUBG-Battlepoint-FarmBot
and download it there <3""")
pause("Just press enter to exit")
