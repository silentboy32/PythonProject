
import threading


def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(6,))
    t2 = threading.Thread(target=print_cube, args=(4,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
