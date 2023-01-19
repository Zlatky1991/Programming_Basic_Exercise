player_name = input()
successful_shots_counter = 0
unsuccessful_shots_counter = 0
points = 301

while points > 0:
    command = input()

    if command == "Retire": # в първата проверка питаме за специалната команда
        print(f"{player_name} retired after {unsuccessful_shots_counter} unsuccessful shots.")
        break

    current_points = int(input())

    if command == "Single": # в следващата проверка питаме дали имаме "Single", "Double" или "Triple"
        current_points = current_points
    elif command == "Double":
        current_points *= 2
    elif command == "Triple":
        current_points = current_points * 3

    if current_points > points:
        unsuccessful_shots_counter += 1
        continue # чрез тази команда програмата започва цикъла отначало
    # ако current_points са по-малко от points тогава преминаваме нататък
    points -= current_points
    successful_shots_counter += 1

if points == 0:
    print(f"{player_name} won the leg with {successful_shots_counter} shots.")
