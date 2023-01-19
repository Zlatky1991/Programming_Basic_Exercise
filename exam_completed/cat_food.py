amount_cats = int(input())
one_kg_food = 12.45

small_cats = 0
big_cats = 0
very_big_cats = 0
total_grams = 0

for i in range(amount_cats):
    grams_food = float(input())

    if 100 <= grams_food < 200:
        small_cats += 1
        total_grams += grams_food
    elif 200 <= grams_food < 300:
        big_cats += 1
        total_grams += grams_food
    elif 300 <= grams_food < 400:
        very_big_cats += 1
        total_grams += grams_food

total_grams = total_grams / 1000
price_per_day = total_grams * one_kg_food

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {very_big_cats} cats.")
print(f"Price for food per day: {price_per_day:.2f} lv.")


