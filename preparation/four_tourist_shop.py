budget = float(input())
product_counter = 0
counter = 0
item_price = 0

name = input()
while name != "Stop":
    price = float(input())
    product_counter += 1
    if price > budget:
        break
    elif product_counter >= 3:
        price /= 2
        budget -= price
        counter += price
    else:
        budget -= price
        counter += price
    name = input()

if price > budget:
    print(f"You bought {product_counter} products for {price} leva.")