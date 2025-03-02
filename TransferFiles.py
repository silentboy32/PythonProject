import os
import shutil

source = "/home/das/PythonProject"
dest = "/home/das/NewPythonProject"

lsdir = os.listdir(source)
for file in lsdir:
    if file.endswith(".py"):
        sources = os.path.join(source,file)
        dests = os.path.join(dest,file)
        
        shutil.copy(sources,dests)
        print(f"Copied {file}")

print("All .py files have been copied.")
