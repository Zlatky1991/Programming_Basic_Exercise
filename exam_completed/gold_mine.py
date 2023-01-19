locations = int(input())
counter = 0


for i in range(locations):
    average_produce = float(input())
    amount_days = int(input())
    for days in range(amount_days):
        kg_produced = int(input())
        counter += kg_produced
    average_amount_gold = counter / amount_days
    counter = 0
    if average_amount_gold >= average_produce:
        print(f"Good job! Average gold per day: {average_amount_gold:.2f}.")
    elif average_amount_gold < average_produce:
        diff = abs(average_amount_gold - average_produce)
        print(f"You need {diff:.2f} gold.")