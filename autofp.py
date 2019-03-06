import pyautogui
from PIL import ImageGrab
from win32 import win32gui
import win32ui, win32con, win32api
from time import sleep
from var_dump import var_dump
def test():
	hwnd = win32gui.FindWindow(None, "NosTale Vendetta")
	if hwnd:
		win32gui.SetForegroundWindow(hwnd)
		x, y, x1, y1 = win32gui.GetClientRect(hwnd)
		x, y = win32gui.ClientToScreen(hwnd, (x, y))
		x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
		img = pyautogui.screenshot(region=(x, y, x1, y1))
		#img.show()
		value = img.getpixel((141,37))
		var_dump(value)

def use_fp(button):
	pyautogui.hotkey('ctrl', button, 'ctrl')
def screen_check(debug):
	hwnd = win32gui.FindWindow(None, "NosTale Vendetta")
	if hwnd:
		win32gui.SetForegroundWindow(hwnd)
		x, y, x1, y1 = win32gui.GetClientRect(hwnd)
		x, y = win32gui.ClientToScreen(hwnd, (x, y))
		x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
		img = pyautogui.screenshot(region=(x, y, x1, y1))
		value = img.getpixel((141,37))
		if(debug == True):
			var_dump(value)
		if value == (9,9,9):
			return True
		else:
			return False

def main():
	pyautogui.alert(text='Automatic Full Potion, cand suntem low hp, scriptul declanșază butonul de FullPot', title='AutoFP', button='Confirm')
	max_fps = pyautogui.prompt(text='Câte full pot-uri dorești să folosești?', title='Do you have FPs?' , default='999')
	waste = pyautogui.confirm(text='Dorești să activezi funcția "anti-waste" pentru a preveni risipa de full pot', title='Anti-Waste', buttons=['da', 'nu'])
	button = pyautogui.confirm(text='Ce buton dorești să folosești? \n Butoanele sunt Ctrl + ', title='Buttons?!', buttons=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
	i = 0
	max_fps = int(max_fps)
	#The Loop
	while(True):
		if(screen_check(False) == True):
			if(i < max_fps):
				use_fp(button)
				i = i + 1
				if(waste == 'da'):
					sleep(5)
			else:
				pyautogui.alert(text='Ai rămas fără poțiuni. Scriptul se oprește', title='AutoFP', button='Confirm')
				exit()

main()
# while True:
	# test()