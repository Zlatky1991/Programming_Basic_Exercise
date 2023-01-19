amount_joinery = int(input())
type_joinery = input()
receiving = input()

amount_joinery1 = 0

if type_joinery == "90X130" and amount_joinery > 60:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 110
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.08)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 110
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.08)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 110
elif type_joinery == "90X130" and amount_joinery > 30:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 110
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.05)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 110
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.05)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 110
elif type_joinery == "100X150" and amount_joinery > 80:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 140
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.1)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 140
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.1)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 140
elif type_joinery == "100X150" and amount_joinery > 40:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 140
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.06)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 140
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.06)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 140
elif type_joinery == "130X180" and amount_joinery > 50:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 190
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.12)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 190
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.12)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 190
elif type_joinery == "130X180" and amount_joinery > 20:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 190
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.07)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 190
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.07)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 190
elif type_joinery == "200X300" and amount_joinery > 50:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 250
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.14)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 250
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.14)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 250
elif type_joinery == "200X300" and amount_joinery > 25:
    if receiving == "Without delivery":
        amount_joinery1 = amount_joinery * 250
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.09)
    elif receiving == "With delivery":
        amount_joinery1 = amount_joinery * 250
        amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.09)
        amount_joinery1 += 60
    else:
        amount_joinery1 = amount_joinery * 250

if amount_joinery < 10:
    print(f"Invalid order")
elif amount_joinery > 99:
    amount_joinery1 = amount_joinery1 - (amount_joinery1 * 0.04)
    print(f"{amount_joinery1:.2f} BGN")
else:
    print(f"{amount_joinery1:.2f} BGN")
