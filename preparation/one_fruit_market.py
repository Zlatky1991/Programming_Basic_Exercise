strawberry_lv = float(input())
bananas_amount_kg = float(input())
oranges_amount_kg = float(input())
raspberry_amount_kg = float(input())
strawberry_amount_kg = float(input())

raspberry_lv = strawberry_lv / 2
oranges_lv = raspberry_lv - (raspberry_lv * 0.4)
bananas_lv = raspberry_lv - (raspberry_lv * 0.8)

raspberry_total = raspberry_amount_kg * raspberry_lv
strawberry_total = strawberry_amount_kg * strawberry_lv
bananas_total =  bananas_amount_kg * bananas_lv
oranges_total = oranges_amount_kg * oranges_lv

total = raspberry_total + strawberry_total + bananas_total + oranges_total

print(f"{total:.2f}")