import time
import pyautogui as pag

focus_position = (695, 137)
pag.click(focus_position)
for i in range(200):
    pag.press('down')
    pag.press('enter')