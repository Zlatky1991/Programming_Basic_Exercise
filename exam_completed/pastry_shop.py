pastry_type = input()
amount_pastry_type = int(input())
day_of_month = int(input())
price_pastries = 0

if day_of_month <= 15:
    if pastry_type == "Cake":
        price_pastries = amount_pastry_type * 24
        if 100 <= price_pastries <= 200:
            price_pastries = price_pastries - (price_pastries * 0.15)
            price_pastries = price_pastries - (price_pastries * 0.1)
        elif price_pastries > 200:
            price_pastries = price_pastries - (price_pastries * 0.25)
            price_pastries = price_pastries - (price_pastries * 0.1)
    elif pastry_type == "Souffle":
        price_pastries = amount_pastry_type * 6.66
        if 100 <= price_pastries <= 200:
            price_pastries = price_pastries - (price_pastries * 0.15)
            price_pastries = price_pastries - (price_pastries * 0.1)
        elif price_pastries > 200:
            price_pastries = price_pastries - (price_pastries * 0.25)
            price_pastries = price_pastries - (price_pastries * 0.1)
    elif pastry_type == "Baklava":
        price_pastries = amount_pastry_type * 12.6
        if 100 <= price_pastries <= 200:
            price_pastries = price_pastries - (price_pastries * 0.15)
            price_pastries = price_pastries - (price_pastries * 0.1)
        elif price_pastries > 200:
            price_pastries = price_pastries - (price_pastries * 0.25)
            price_pastries = price_pastries - (price_pastries * 0.1)
elif 15 < day_of_month <= 22:
    if pastry_type == "Cake":
        price_pastries = amount_pastry_type * 28.70
        if 100 <= price_pastries <= 200:
            price_pastries = price_pastries - (price_pastries * 0.15)
        elif price_pastries > 200:
            price_pastries = price_pastries - (price_pastries * 0.25)
    elif pastry_type == "Souffle":
        price_pastries = amount_pastry_type * 9.8
        if 100 <= price_pastries <= 200:
            price_pastries = price_pastries - (price_pastries * 0.15)
        elif price_pastries > 200:
            price_pastries = price_pastries - (price_pastries * 0.25)
    elif pastry_type == "Baklava":
        price_pastries = amount_pastry_type * 16.98
        if 100 <= price_pastries <= 200:
            price_pastries = price_pastries - (price_pastries * 0.15)
        elif price_pastries > 200:
            price_pastries = price_pastries - (price_pastries * 0.25)
elif 22 < day_of_month < 25:
    if pastry_type == "Cake":
        price_pastries = amount_pastry_type * 28.7
    elif pastry_type == "Souffle":
        price_pastries = amount_pastry_type * 9.8
    elif pastry_type == "Baklava":
        price_pastries = amount_pastry_type * 16.98

print(f"{price_pastries:.2f}")
