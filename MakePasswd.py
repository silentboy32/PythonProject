
import random

#First import random module
#Here character set for make passwd

#Char = "thebrownfoxjumpsoverthelazydog"
Number = "1234567890"
#Symbols = "@#&"
#Capital_Char = Char.upper()

#MixedChar = Char + Number + Symbols + Capital_Char


usr = (input("Enter your mobile No. "))

passwd = ""

if len(usr) == 10:
    for _ in range(4):
        passwd += random.choice(Number)
    
else:
    print("Invalid Number ")


print(passwd)





# Length = int(input("Enter Length of Passwd "))

# #Main code here
# #Used // "".join() Method 
# #Random module for chose random value

# passwd = "".join(random.sample(MixedChar,Length))

# print(f"This is passwd => {passwd}")

# #There will be occured final passwd
