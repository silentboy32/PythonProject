import random
import pyautogui

def randoms():
    rand = ""
    lists = "123456790"
    for i in range(4):
        rand += random.choice(lists)

    return rand

def Screen(name):
    names = f"screen-{name}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(names)
    #print(names)

value = randoms()
Screen(value)




