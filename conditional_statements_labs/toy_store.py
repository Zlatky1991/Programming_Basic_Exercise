vaca_price = float(input())
puzzle_amount = int(input())
dolls_amount = int(input())
bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

price = puzzle_amount * 2.6 + dolls_amount * 3 + bears_amount * 4.1 + minions_amount * 8.2 + trucks_amount * 2
toys_amount = puzzle_amount + dolls_amount + bears_amount + minions_amount + trucks_amount

if toys_amount >= 50:
    price -= price * 0.25
price -= price * 0.1

if price >= vaca_price:
    print(f'Yes! {price - vaca_price:.2f} lv left.')
else:
    print(f'Not enough money! {vaca_price - price:.2f} lv needed.')

