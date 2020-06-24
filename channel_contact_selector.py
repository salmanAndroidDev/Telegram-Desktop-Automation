import time
import pyautogui as pag

focus_position = (695, 137)
pag.click(focus_position)
for i in range(187):
    pag.press('down')
    pag.press('enter')