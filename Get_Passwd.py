import random 

char = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbols = "~!@#$%^&*()_+<>,.?"

mixedChar = char + number + symbols

passwd = ""

lenght = int(input("Enter your lenght of Passwd "))
for _ in range(lenght):
    passwd += random.choice(mixedChar)

print()
print(f"**** {passwd} ******")
print()
