
names = []
while True:
    usr = input("Enter your name ")
    if usr == "":
        break
    else:
        names.append(usr)

print()
i = 1
for item in names:
    print(f"{i} {item.title()}")
    i += 1
