# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# •	Ако  парите за декора и дрехите са повече от бюджета:
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:

movie_budget = float(input())
number_actors = int(input())
suit_price = float(input())

decor = movie_budget * 0.1
total_suit_price = number_actors * suit_price

if number_actors > 150:
    total_suit_price -= total_suit_price * 0.1

amount_needed = decor + total_suit_price

if amount_needed > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {amount_needed - movie_budget:.2f} leva more.")
elif amount_needed <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - amount_needed:.2f} leva left.")
