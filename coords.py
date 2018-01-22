import time, pyautogui
def coordinadas():
	"""
	Click cancel in the rejoin msg
	"""
	file22 = open("input.txt" , "r", encoding="utf-8")
	lines22 = file22.readlines()
	x = lines22[0]
	a, b = x.split()
	int(a)
	int(b)
	time.sleep(10)
	pyautogui.click((a,b))
def salir():
	"""
	If you die click exit to lobby
	"""
	file23 = open("input.txt" , "r", encoding="utf-8")
	lines23 = file23.readlines()
	y = lines23[1]
	c, d = y.split()
	int(c)
	int(d)
	time.sleep(1)
	pyautogui.click((c,d))