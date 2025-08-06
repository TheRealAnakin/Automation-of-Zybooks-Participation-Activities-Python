import pyautogui as pyag
import time 
import pyperclip

pyperclip.copy(open("AutomateCode.js", "r").read())

pyag.hotkey('alt','tab')

def main():
    time.sleep(2)
    pyag.hotkey('ctrl','shift','i')   
    time.sleep(2)
    pyag.hotkey('ctrl','v','enter')
    time.sleep(1)
    pyag.hotkey('ctrl','shift','i') 
    time.sleep(3)
    pyag.hotkey('ctrl','shift','i')
    time.sleep(1)
    pyag.hotkey('ctrl','tab')
    time.sleep(1)
    pyag.hotkey('ctrl','v','enter')
    time.sleep(5)
    print("Main Function Complete!")


main()


