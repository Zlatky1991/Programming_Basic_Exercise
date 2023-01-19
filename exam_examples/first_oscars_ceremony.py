hall_rent = int(input())
#Статуетки – цената им е 30% по-малка от наема на залата
oscars_price = hall_rent - (hall_rent * 0.30)
#Кетъринг – цената му е 15% по-малка от тази на статуетките
catering_price = oscars_price - (oscars_price * 0.15)
#Озвучаване – цената му е 1 / 2 от цената за кетъринг
price_for_sounding = catering_price / 2

total_cost = hall_rent + oscars_price + catering_price + price_for_sounding
#Сумата да бъде форматирана до втория знак след десетичния знак.
print(f"{total_cost:.2f}")
