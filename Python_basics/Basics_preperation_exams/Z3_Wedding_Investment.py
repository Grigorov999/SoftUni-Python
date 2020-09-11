contract_duration = input()
contract_type = input()
desert = input()
count_months_for_payment = int(input())

price = 0.0
desert_price = 0.0
current_price = 0.0

if contract_duration == 'one':
    if contract_type == 'Small':
        price = 9.98
    elif contract_type == 'Middle':
        price = 18.99
    elif contract_type == 'Large':
        price = 25.98
    elif contract_type == 'ExtraLarge':
        price = 35.99
elif contract_duration == 'two':
    if contract_type == 'Small':
        price = 8.58
    elif contract_type == 'Middle':
        price = 17.09
    elif contract_type == 'Large':
        price = 23.59
    elif contract_type == 'ExtraLarge':
        price = 31.79

if desert == 'yes':
    if price <= 10.00:
        desert_price = 5.50
        current_price = price + desert_price
    elif 10.00 < price <= 30.00:
        desert_price = 4.35
        current_price = price + desert_price
    elif price > 30.00:
        desert_price = 3.85
        current_price = price + desert_price
if desert == 'no':
    current_price = price

if contract_duration == 'one':
    total = count_months_for_payment * current_price
    print(f'{total:.2f} lv.')

if contract_duration == 'two':
    total = count_months_for_payment * current_price
    discounted_total = total - ((total * 3.75) / 100)
    print(f'{discounted_total:.2f} lv.')
