from os import system
import os 

listfile = os.listdir()

#c = cat listfile
for i in listfile:
     result = system(f"cat {i}")
     print(result)
     print("____________________________________________")
