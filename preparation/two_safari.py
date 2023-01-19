budget = float(input())
liter_gasoline = float(input())
day_of_the_week = input()

price_gasoline = 0
total_price = 0
discount = 0
if day_of_the_week == "Saturday":
    price_gasoline = liter_gasoline * 2.1
    total_price = price_gasoline + 100
    total_price -= (total_price * 0.1)
elif day_of_the_week == "Sunday":
    price_gasoline = liter_gasoline * 2.1
    total_price = price_gasoline + 100
    total_price -= (total_price * 0.2)
else:
    price_gasoline = liter_gasoline * 2.1
    total_price = price_gasoline + 100

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")