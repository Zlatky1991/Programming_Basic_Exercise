
club_income = 0

desired_profit = float(input())

while True:
    cocktail_name = input()

    if cocktail_name == "Party!":
        print(f"We need {desired_profit - club_income:.2f} leva more.")
        print(f"Club income - {club_income:.2f} leva.")
        break

    cocktail_amount_per_order = int(input())

    cocktail_name = len(cocktail_name)
    total_cocktail_price = cocktail_name * cocktail_amount_per_order
    if total_cocktail_price % 2 != 0:
        total_cocktail_price = total_cocktail_price - (total_cocktail_price * 0.25)

    club_income += total_cocktail_price

    if club_income >= desired_profit:
        print(f"Target acquired.")
        print(f"Club income - {club_income:.2f} leva.")
        break