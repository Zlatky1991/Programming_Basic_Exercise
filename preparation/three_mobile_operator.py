term_of_the_contract = input()
type_contract = input()
added_mobile_internet = input()
months_amount = int(input())

one_year_contract_price = 0
total = 0

if term_of_the_contract == "one" and added_mobile_internet == "yes":
    if type_contract == "Small":
        one_year_contract_price = 9.98
        if one_year_contract_price <= 10:
            one_year_contract_price += 5.5
            total = months_amount * one_year_contract_price
    elif type_contract == "Medium":
        one_year_contract_price = 18.99
        if one_year_contract_price <= 30:
            one_year_contract_price += 4.35
            total = months_amount * one_year_contract_price
    elif type_contract == "Large":
        one_year_contract_price = 25.98
        if one_year_contract_price <= 30:
            one_year_contract_price += 4.35
            total = months_amount * one_year_contract_price
    elif type_contract == "ExtraLarge":
        one_year_contract_price = 35.99
        if one_year_contract_price > 30:
            one_year_contract_price += 3.85
            total = months_amount * one_year_contract_price
elif term_of_the_contract == "one" and added_mobile_internet == "no":
    if type_contract == "Small":
        one_year_contract_price = 9.98
        total = months_amount * one_year_contract_price
    elif type_contract == "Medium":
        one_year_contract_price = 18.99
        total = months_amount * one_year_contract_price
    elif type_contract == "Large":
        one_year_contract_price = 25.98
        total = months_amount * one_year_contract_price
    elif type_contract == "ExtraLarge":
        one_year_contract_price = 35.99
        total = months_amount * one_year_contract_price
elif term_of_the_contract == "two" and added_mobile_internet == "yes":
    if type_contract == "Small":
        one_year_contract_price = 8.58
        if one_year_contract_price <= 10:
            one_year_contract_price += 5.5
            total = months_amount * one_year_contract_price
            total -= total * 0.0375
    elif type_contract == "Medium":
        one_year_contract_price = 17.09
        if one_year_contract_price <= 30:
            one_year_contract_price += 4.35
            total = months_amount * one_year_contract_price
            total -= total * 0.0375
    elif type_contract == "Large":
        one_year_contract_price = 23.59
        if one_year_contract_price <= 30:
            one_year_contract_price += 4.35
            total = months_amount * one_year_contract_price
            total -= total * 0.0375
    elif type_contract == "ExtraLarge":
        one_year_contract_price = 31.79
        if one_year_contract_price > 30:
            one_year_contract_price += 3.85
            total = months_amount * one_year_contract_price
            total -= total * 0.0375
elif term_of_the_contract == "two" and added_mobile_internet == "no":
    if type_contract == "Small":
        one_year_contract_price = 8.58
        total = months_amount * one_year_contract_price
        total -= total * 0.0375
    elif type_contract == "Medium":
        one_year_contract_price = 17.09
        total = months_amount * one_year_contract_price
        total -= total * 0.0375
    elif type_contract == "Large":
        one_year_contract_price = 23.59
        total = months_amount * one_year_contract_price
        total -= total * 0.0375
    elif type_contract == "ExtraLarge":
        one_year_contract_price = 31.79
        total = months_amount * one_year_contract_price
        total -= total * 0.0375

print(f"{total:.2f} lv.")
