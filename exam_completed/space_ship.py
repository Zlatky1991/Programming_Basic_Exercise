width = float(input())
length = float(input())
high = float(input())
average_high = float(input())
import math

volume_rocket = width * length * high
volume_room = (average_high + 0.40) * 2 * 2
total_space_for = math.floor(volume_rocket / volume_room)

if 3 <= total_space_for <= 10:
    print(f"The spacecraft holds {total_space_for} astronauts.")
elif total_space_for < 3:
    print(f"The spacecraft is too small.")
else:
    print(f"The spacecraft is too big.")
