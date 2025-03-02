
import time

inter_time = int(input("Enter time _"))


while inter_time:
    mint,secs = (divmod(inter_time,60))
    time_format = f"{mint:02d}:{secs:02d}"

    print(time_format, end="\r")
    time.sleep(1)
    inter_time -= 1

print("Time's up !")
