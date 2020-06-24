import time
import pyautogui as pag


def add_contacts():
    iconXY = pag.locateOnScreen('./people.png')
    backXY = (547, 116)
    save_contact = (833, 582)

    pag.moveTo(iconXY)
    pag.moveRel(0,-30)
    pag.click()

    for j in range(200):  
        for i in range(3):
            pag.press('down')
            # time.sleep(2)
        curren_screen = pag.position()
        pag.click()
        time.sleep(0.5)

        addXY = pag.locateOnScreen('./add_contact.png')
        
        if addXY:
            pag.click(addXY)
            time.sleep(0.5)
            pag.click(save_contact)
            time.sleep(1.8)
        
        pag.click(backXY)
        time.sleep(0.5)


        pag.moveTo(curren_screen)

add_contacts()