import time
import pyautogui as pag



"""
You can take screenshot and crop the position where you would like to be clicked and find it's x and y 
like this one below, but it takes time i prefere to hard code x and y of positions i like to be clicked.
...
menu_loc = pag.locateOnScreen('./setting.png')
"""
waint = 0.4
def delete_user():
    menuXY = (95, 82)
    contactsXY = (168, 312)
    contact_profile_nameXY = (588, 79)
    verify_delete = (825, 455)
    exit_profile  = (885, 117)
    focus_profle_XY = (643, 108)

    pag.click(menuXY)
    time.sleep(waint)
    pag.click(contactsXY)
    time.sleep(waint)
    pag.press('down')
    time.sleep(waint)
    pag.press('enter')
    time.sleep(waint)
    pag.click(contact_profile_nameXY)

    deleteXY = pag.locateOnScreen('delete.png')
    if deleteXY == None:
        for j in range(10):
            pag.click(focus_profle_XY)            
            pag.press('down')
            pag.press('down')
            deleteXY = pag.locateOnScreen('delete.png')
            
            if deleteXY == None:
                break

    pag.click(deleteXY)
    time.sleep(waint)
    pag.click(verify_delete)
    pag.click(exit_profile)
    time.sleep(waint)
