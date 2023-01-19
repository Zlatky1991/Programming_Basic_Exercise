amount_food_bought = int(input())
amount_food_bought_grams = amount_food_bought * 1000
grams_collected = 0

#На всеки следващ ред до получаване на команда Adopted
# ще получавате колко грама изяжда кученцето на всяко хранене - цяло число в интервала [10 …1000]
while True:
    command = input()
    if command == "Adopted":
        break
    command = int(command)
    grams_collected += command

diff = abs(grams_collected - amount_food_bought_grams)
if grams_collected <= amount_food_bought_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")