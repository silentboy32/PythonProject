import time
import pyautogui as pr

msg = input("Enter your msg ")
times = int(input("Enter number "))


time.sleep(10)

for i in range(times):
    pr.write(msg)
    pr.press("enter")
