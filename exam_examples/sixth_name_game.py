best_player = ""
best_player_score = 0
while True:
    name = input()

    if name == "Stop":
        break

    current_sum = 0

    for ch in name:
        current_number = int(input())

        if current_number == ord(ch): # ако е равна на стойността на буквата в ASCI таблицата
            current_sum += 10
        else:
            current_sum += 2

    if current_sum >= best_player_score:
        best_player_score = current_sum
        best_player = name

print(f"The winner is {best_player} with {best_player_score} points!")


