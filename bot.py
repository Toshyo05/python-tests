import pyautogui
import random
import time


while True:
    x = random.randint(500, 900)
    y = random.randint(500, 900)

    pyautogui.moveTo(x, y, 0.5)
    
    time.sleep(2)