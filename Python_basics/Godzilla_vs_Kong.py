budget = float(input())
statist_count = float(input())
price_clothes = float(input())

decour = budget * 0.1
clothes_all = statist_count * price_clothes

if statist_count > 150:
    clothes_all *= 0.9

expenses = decour + clothes_all

if (expenses) > budget:
    print(f'Not enough money! \n Wingard needs {(expenses - budget):.2f} leva more.')
else:
    print(f'Action! \n Wingard starts filming with {budget - expenses:.2f} leva left.')
