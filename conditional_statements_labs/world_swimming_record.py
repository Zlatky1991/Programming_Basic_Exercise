# Рекордът в секунди – реално число;
# Разстоянието в метри – реално число;
# Времето в секунди, за което плува разстояние от 1 м. - реално число.
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди

# •	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# •	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:

from math import floor

world_record = float(input())
distance_in_meter = float(input())
time_in_seconds = float(input())

new_record = distance_in_meter * time_in_seconds
slowing_down = floor(distance_in_meter / 15) * 12.5

swimming_record = new_record + slowing_down

if swimming_record < world_record:
    print(f"Yes, he succeeded! The new world record is {swimming_record:.2f} seconds.")
elif swimming_record >= world_record:
    print(f"No, he failed! He was {swimming_record - world_record:.2f} seconds slower.")
