# Python Count Down Timer
import time

user_time = int(input("Enter time ⏲ in seconds: "))

# for counter in reversed(range(0, user_time + 1)):
#     time.sleep(1)
#     print(f"Tick Tack ⏲: {counter}")

# print(f"Time is Up! {counter} second completed ⌛")

# for counter in (range(user_time, 0, -1)):
#     time.sleep(1)
#     print(f"Tick Tack ⏲: {counter}")

# print(f"Time is Up! {counter} second completed ⌛")

for counter in (range(user_time, 0, -1)):
    time.sleep(1)
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"⏲: {hours:02}:{minutes:02}:{seconds:02}") # format specifier add zero padding

print(f"Time is Up! {counter} second completed ⌛")
