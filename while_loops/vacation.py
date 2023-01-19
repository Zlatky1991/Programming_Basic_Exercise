needed_money = float(input())
owned_money = float(input())

day_count = 0
spending_counter = 0

while True:
    command = input()
    current_money = float(input())
    day_count += 1

    if command == "save":
        owned_money += current_money
        spending_counter = 0
    elif command == "spend":
        spending_counter += 1
        owned_money -= current_money
        if owned_money < 0:
            owned_money = 0
    if spending_counter == 5:
        print(f"You can't save the money.")
        print(day_count)
        break

    if owned_money >= needed_money:
        print(f"You saved the money for {day_count} days.")
        break