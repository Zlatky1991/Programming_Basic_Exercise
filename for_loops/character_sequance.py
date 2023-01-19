number = int(input())

for i in range(1, number, 10):
    current_number = int(input())
    if current_number % 2 == 0:
        print(current_number)