#Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
destination = input()
#Втори ред - дати, през които си е резервирала екскурзията - текст с възможности "21-23",
#"24-27" или "28-31"
data = input()
#Трети ред - брой нощувки - цяло число в интервала [1… 100]
numbers_of_nights = int(input())

total_cost = 0

if destination == "France":
    if data == "21-23":
        total_cost = numbers_of_nights * 30
    elif data == "24-27":
        total_cost = numbers_of_nights * 35
    elif data == "28-31":
        total_cost = numbers_of_nights * 40
elif destination == "Italy":
    if data == "21-23":
        total_cost = numbers_of_nights * 28
    elif data == "24-27":
        total_cost = numbers_of_nights * 32
    elif data == "28-31":
        total_cost = numbers_of_nights * 39
elif destination == "Germany":
    if data == "21-23":
        total_cost = numbers_of_nights * 32
    elif data == "24-27":
        total_cost = numbers_of_nights * 37
    elif data == "28-31":
        total_cost = numbers_of_nights * 43

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")

