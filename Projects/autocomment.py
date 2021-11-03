import pyautogui
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
comments = "@name1 @name @name"
time.sleep(5)

for i in range(200):
    if i <= 5:
        pyautogui.typewrite(comments)
        pyautogui.typewrite("\n")
        pyautogui.click(button='left')
        time.sleep(42)
    elif 5 <= i <= 10:
        pyautogui.typewrite(comments)
        pyautogui.typewrite("\n")
        pyautogui.click(button='left')
        time.sleep(54)
    else:
        pyautogui.typewrite(comments)
        pyautogui.typewrite("\n")
        pyautogui.click(button='left')
        time.sleep(60)
print(f"Program finished at: {current_time}")



