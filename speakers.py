import pyautogui
from time import sleep
from win32 import win32gui

def foreground():
	nostale = win32gui.FindWindow(None, "NosTale Vendetta")
	if nostale:
		win32gui.SetForegroundWindow(nostale)

def spekermsg(msg, button):
	foreground()
	sleep(0.1)
	pyautogui.hotkey('ctrl', button, 'ctrl')
	sleep(0.2)
	pyautogui.typewrite("  "+msg, interval=0.10)
	pyautogui.press("enter")

def times():
	try:
		cat = pyautogui.prompt(text='How many spekers do you want to send?', title='How many?!', default='999')
		cat = int(cat)
		return cat
	except ValueError:
		times()

def main():
	cat = times()
	msg = pyautogui.prompt(text='Enter the message for the speaker (maximum 120 characters) will be sent :'+format(cat), title='Speaker Message' , default='')
	button = pyautogui.confirm(text='What button do you want to use? \n Buttons are Ctrl + 1 2 3 4 5 6 7 8 9 0 (first row from above)', title='Buttons?!', buttons=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
	msg_s = len(msg)
	pyautogui.alert(text='Lets see if I get it right ... You want to send the message\n'+msg+' ('+format(msg_s)+'/120 characters)\n x '+format(cat), button='Confirm')
	if(msg_s < 120):
		i = 0
		while(i < cat):
			i = i + 1
			spekermsg(msg, button)
			print("Was sent "+format(i)+" speakere")
			sleep(60)
		print("Finished")
		exit()
	else:
		pyautogui.alert(text='The message you entered is too large!', title='Error', button='Try again')
		main()
main()