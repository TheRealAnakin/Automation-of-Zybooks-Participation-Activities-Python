import pyautogui
import time
import pyperclip

def getMousePosition():
    time.sleep(5)
    m = pyautogui.position()
    position = (m.x,m.y)
    pyperclip.copy(position)



getMousePosition()











    
