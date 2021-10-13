import pyautogui
import time

comments = "@elena_strantari @george.gazetis @ntos_"

time.sleep(5)

for i in range(20000):
    pyautogui.typewrite(comments)
    pyautogui.click(button='left')
    time.sleep(5)