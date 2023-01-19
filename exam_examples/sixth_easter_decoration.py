number_of_clients = int(input())
total_sum_for_all_orders = 0
# Цените на продуктите са:
#  кошничка за яйца (basket) – 1.50 лв.
#  великденски венец (wreath) – 3.80 лв.
#  шоколадов заек (chocolate bunny) – 7 лв.

# От конзолата първоначално се чете един ред:
#  Брои на клиентите в магазина – цяло число [1… 100]
#  След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
#  Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")
for count in range(number_of_clients):
    current_sum = 0
    product_counter = 0

    while True:
        product = input()

        if product == "Finish":
            break

        product_counter += 1 # отброяваме броя закупени продукти

        if product == "basket":
            current_sum += 1.5
        elif product == "wreath":
            current_sum += 3.80
        elif product == "chocolate bunny":
            current_sum += 7

    if product_counter % 2 == 0: # всеки клиент закупил четен брой продукти, ще получи 20% отстъпка от крайната цена.
        current_sum = current_sum - (current_sum * 0.20)

    total_sum_for_all_orders += current_sum
    print(f"You purchased {product_counter} items for {current_sum:.2f} leva.")

# total_sum_for_all_orders /= number_of_clients
total_sum_for_all_orders = total_sum_for_all_orders / number_of_clients #излизаме от цикъла и пресмятаме
print(f"Average bill per client is: {total_sum_for_all_orders:.2f} leva.")
