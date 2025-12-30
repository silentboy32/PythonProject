import pyautogui as do
import time

#msg = input("Hello Samar Barman")
msg = "Hello Samar Barman"

time.sleep(10)

for _ in range(10):
    do.write(msg)
    do.press("Enter")

