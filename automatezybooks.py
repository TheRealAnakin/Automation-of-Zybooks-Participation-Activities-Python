import pyautogui
import time
from PIL import Image 
import PIL
from playsound import playsound
import pyperclip


print("Welcome to ZyBooks automated! We fucking hate this platform too, and schooling in general.")
print("Enter your amount of iterations!:")
amountofsteps = int(input())

openText = open('information.txt','r')
text = openText.read()

pyperclip.copy(text)

pyautogui.hotkey('alt','tab')

def automate():
    time.sleep(4)
    pyautogui.click(2324, 101)
    time.sleep(1)
    pyautogui.click(2162, 177)
    pyautogui.click(1254, 442)
    pyautogui.hotkey('ctrl','shift','i')
    time.sleep(3)
    pyautogui.click(2051, 1408)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl','shift','i')
    time.sleep(15)
    pyautogui.scroll(-10000)
    time.sleep(1)
    pyautogui.click(1764, 1413)
    pyautogui.click(1702, 1358)

playsound('/home/estefany/Downloads/GoyardPython.mp3')


for i in range (0,amountofsteps):
    automate()
    print(i)
    if i == amountofsteps:
        playsound('/home/estefany/Downloads/GoyardPython.mp3')

print("finished!")            
"""
def jumpStep():
    time.sleep(1)
    pyautogui.click(171, 182)
    time.sleep(1)
    pyautogui.click(887, 481)
    time.sleep(2)
    percentages = pyautogui.screenshot(region=(1450, 369, 1078, 70))
    percentagesImage =  percentages.save("percentages.png")
 """   
