from datetime import datetime
import pyautogui
import random


def move_cursor():
    for n in range(1,1000):
        x = random.randint(1, 1920)
        y = random.randint(1, 1080)
        pyautogui.moveTo(x, y)
        pyautogui.click()

        time = datetime.now().strftime("%H:%M:%S")

        print(f"Moving to {x}, {y} at {time}")
        pyautogui.sleep(10)

move_cursor()