n = int(input())
salary = int(input())


for i in range(1, n + 1):
    name = input()

    if name == "Facebook":
        salary = salary - 150
    elif name == "Instagram":
        salary = salary - 100
    elif name == "Reddit":
        salary = salary - 50
    elif salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")
