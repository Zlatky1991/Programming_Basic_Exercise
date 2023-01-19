balls_amount = int(input())
total_points = 0
red, orange, yellow, white, = 0, 0, 0, 0
other_colors_picked = 0
divided = 0

import math # import-ваме math за да закръгляме към по-малкото цяло число.
# ако искаме да закръгляме към по-голямото цяло число използваме math.ceil
for i in range(balls_amount):
    color = input()

    if color == "red":
        red += 1
        total_points += 5
    elif color == "orange":
        orange += 1
        total_points += 10
    elif color == "yellow":
        yellow += 1
        total_points += 15
    elif color == "white":
        white += 1
        total_points += 20
    elif color == "black":
        divided += 1
        total_points = math.floor(total_points / 2) # закръгляме към по-малкото цяло число.
    else:
        other_colors_picked += 1
        total_points = total_points

print(f"Total points: {total_points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other_colors_picked}")
print(f"Divides from black balls: {divided}")









