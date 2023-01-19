amount_climbers = int(input())

musala = 0
kilimandjaro = 0
monblan = 0
k2 = 0
everest = 0
total_amount = 0

for i in range(amount_climbers):
    amount_people = int(input())

    total_amount += amount_people

    if amount_people <= 5:
        musala += amount_people
    elif 6 <= amount_people <= 12:
        monblan += amount_people
    elif 13 <= amount_people <= 25:
        kilimandjaro += amount_people
    elif 26 <= amount_people <= 40:
        k2 += amount_people
    else:
        everest += amount_people

total_musala = musala / total_amount * 100
total_monblan = monblan / total_amount * 100
total_kilimandjaro = kilimandjaro / total_amount * 100
total_k2 = k2 / total_amount * 100
total_everest = everest / total_amount * 100

print(f"{total_musala:.2f}%")
print(f"{total_monblan:.2f}%")
print(f"{total_kilimandjaro:.2f}%")
print(f"{total_k2:.2f}%")
print(f"{total_everest:.2f}%")