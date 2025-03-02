
import string
import time

abcd = (string.ascii_lowercase[:])

a1 = ""
a2 = ""
a3 = ""
a4 = ""

for i in abcd:
    if i == "h":
        a1 += "h"
    if i == "e":
        a2 += "e"
    if i == "l":
        a3 += "ll"
    if i == "o":
        a4 += "o"
    print(f"{a1}{a2}{a3}{a4}")
    time.sleep(0.17)
