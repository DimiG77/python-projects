import pyautogui
import time

comments = "name_1, Name_2, Name_3"

time.sleep(5)

for i in range(20000):
    pyautogui.typewrite(comments)
    pyautogui.typewrite("\n")
    pyautogui.click(button='left')
    time.sleep(50)
