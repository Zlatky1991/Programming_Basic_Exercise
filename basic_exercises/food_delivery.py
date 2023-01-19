amount_chicken_menu = int(input())
amount_fish_menu = int(input())
amount_veggie_menu = int(input())

price_chicken_menu = amount_chicken_menu * 10.35
price_fish_menu = amount_fish_menu * 12.4
price_veggie_menu = amount_veggie_menu * 8.15

total_price = price_veggie_menu + price_fish_menu + price_chicken_menu

dessert_price = total_price * 0.2

final_amount = total_price + dessert_price + 2.5

print(f"{final_amount:.2f}")