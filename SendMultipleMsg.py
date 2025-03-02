import pyautogui as do
import time

msg = input("Enter the Msg....")

time.sleep(10)

for _ in range(50):
    do.write(msg)
    do.press("Enter")

