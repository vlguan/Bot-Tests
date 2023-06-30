from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
# TILE1 1700 1200
# TILE2 1600 1200
# TILE3 1800 1200
# TILE4 2000 1200
color_of_tile = 100
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')== False:
    if pyautogui.pixel(1400, 700)[0] < color_of_tile:
        click(1400, 700)
    if pyautogui.pixel(1600, 700)[0] < color_of_tile:
        click(1600, 700)
    if pyautogui.pixel(1800, 700)[0] < color_of_tile:
        click(1800, 700)
    if pyautogui.pixel(2000, 700)[0] < color_of_tile:
        click(2000, 700)
