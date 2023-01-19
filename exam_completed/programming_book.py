print_price_per_page = float(input())
print_price_per_board = float(input())
discount_percent = int(input())
amount_to_pay_for_designer = float(input())
percent_total_amount = int(input())

starting_price_to_print = print_price_per_page * 899 + print_price_per_board * 2
price_after_discount = starting_price_to_print - (starting_price_to_print * (discount_percent / 100))
amount_for_designer = price_after_discount + amount_to_pay_for_designer
total_price = amount_for_designer - (amount_for_designer * (percent_total_amount / 100))

print(f"Avtonom should pay {total_price:.2f} BGN.")
