
def incode(msg):
    msgs = ""
    for i in msg:
        msgs += str(f"{ord(i)}#")
        

    return msgs


def Decode(msg):
    pd = msg.split("#")
    
    result = ""

    for i in pd:
        if i != "":
            result += (chr(int(i)))

    return result
        


print()
print("Note: you can use 1 for continue or 2 for exit")
print()
while True:
    print()
    ints = input("What want you exit or continue ")

    if ints == "continue" or ints == "1":
        print()
        massge = input("Put Your Msg__")

        usr = input("For incode Press 1 \nFor Decode Press 2 ")
        if usr == "1":
            msg = incode(massge)
            print(f"Here Your Decript Msg => {msg}")
        else:
            m = Decode(massge)
            print(f"Here Your Incript Msg => {m}")
    else:
        break
