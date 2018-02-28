import time, pyautogui
def coordinadas():
	"""
	Click cancel in the rejoin msg
	"""
	try:
		file22 = open("input.txt" , "r", encoding="utf-8")
		lines22 = file22.readlines()
		x = lines22[0]
		a, b = x.split()
		int(a)
		int(b)
		time.sleep(3) #Change the number between () if your pc doesnt click the rejoin cancel button put a higher number
		pyautogui.click((a,b))
		time.sleep(2)
		pyautogui.click((a,b))
		time.sleep(2)
		pyautogui.click((a,b))
		print('Click on cancel just i case that the reconnect button is there')
	except IndexError:
		print('You don´t have the coords for clicking the cancel button')

def salir():
	"""
	If you die click exit to lobby
	"""
	try:
		file23 = open("input.txt" , "r", encoding="utf-8")
		lines23 = file23.readlines()
		y = lines23[1]
		c, d = y.split()
		int(c)
		int(d)
		time.sleep(1)
		pyautogui.click((c,d))
		time.sleep(1)
		pyautogui.click((c,d))
		time.sleep(1)
		pyautogui.click((c,d))
		print('Click on leave game jus in case that you died')
	except IndexError:
		print('You don´t have the coords for leaving the game in case you are dead')
def busy():
	"""
	If servers are busy click
	"""
	try:
		file24 = open("input.txt" , "r", encoding="utf-8")
		lines24 = file24.readlines()
		z = lines24[2]
		e, f = z.split()
		int(e)
		int(f)
		time.sleep(2)
		pyautogui.click((e,f))
		time.sleep(2)
		pyautogui.click((e,f))
		print('Click the reconnect msg in case servers are busy')
	except IndexError:
		print('You don´t have the coords for servers are busy')
def showbps(numero, actual_time):
	f = open('BPs won %s.txt'%actual_time,'w')
	f.write("Total BPs won" + numero)
	f.close
