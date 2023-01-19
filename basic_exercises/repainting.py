nylon_needed = int(input())
paint_needed_lt = int(input())
diluent_needed_lt =  int(input())
hours_needed = int(input())

nylon_price = ((nylon_needed) + 2) * 1.5

paint_price = ((paint_needed_lt) + (paint_needed_lt * 0.10)) * 14.5

price_for_diluent = (diluent_needed_lt) * 5.00

total_price_for_materials = nylon_price + paint_price + price_for_diluent + 0.40

price_for_workers = (total_price_for_materials * 0.3) * hours_needed

final_price = total_price_for_materials + price_for_workers

print(final_price)