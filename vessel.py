import pyautogui
import win32gui
import sys
import threading
from multiprocessing import Process
from time import sleep

def get_screen_info():
    hwnd = win32gui.FindWindow(None, "NosTale Vendetta")
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        x, y, x1, y1 = win32gui.GetClientRect(hwnd)
        x, y = win32gui.ClientToScreen(hwnd, (x, y))
        x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
        img = pyautogui.screenshot(region=(x, y, x1, y1))
        if(img.getpixel((722, 17)) == (2,2,2,)):
            return True
        else:
            return False

def auto_attack():
    pyautogui.press('space')
    sleep(0.1)
    pyautogui.press('space')
    pyautogui.press('space')

def summon_vessel():
    if(get_screen_info() == False):
        sleep(2)
        pyautogui.hotkey('ctrl', '0')
        sleep(3)
        auto_attack()

def skill_buff():
    sleep(1)
    pyautogui.press('Q')
    sleep(3)
    pyautogui.press('6')
    sleep(3)
    pyautogui.press('5')
    sleep(300)

def skill_0():
    pyautogui.press('2')
    sleep(7.4)

def skill_1():
    pyautogui.press('3')
    sleep(26)

def skill_2():
    pyautogui.press('w')
    sleep(111)

def skill_3():
    pyautogui.press('e')
    sleep(32.5)

def skill_4():
    pyautogui.press('r')
    sleep(61)

def skill_5():
    pyautogui.hotkey('shift', 'e')
    sleep(61)

if __name__ == '__main__':
    a = Process(target=summon_vessel)
    a.start()
    a.join()
    b = Process(target=skill_buff)
    a.join(b)
    c = Process(target=skill_0)
    a.join(c)
    d = Process(target=skill_1)
    a.join(d)
    e = Process(target=skill_2)
    a.join(e)
    f = Process(target=skill_3)
    a.join(f)
    g = Process(target=skill_4)
    a.join(g)
    h = Process(target=skill_5)
    a.join(h)