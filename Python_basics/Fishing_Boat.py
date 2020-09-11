budget = int(input())
season = input()
fisher_count = int(input())

boat_price = 0.0

if season == 'Spring':
    boat_price = 3000.00
elif season == 'Summer':
    boat_price = 4200.00
elif season == 'Autumn':
    boat_price = 4200.00
elif season == 'Winter':
    boat_price = 2600.00

discount = 0.0
if fisher_count <= 6:
    discount = 0.1
elif fisher_count <= 11:
    discount = 0.15
else:
    discount = 0.25

discount_val = boat_price * discount
expenses = boat_price - discount_val

if fisher_count % 2 == 0 and season != 'Spring':
    expenses = expenses * 0.95

if budget >= expenses:
    print(f'Yes! You have {(budget - expenses):.2f} leva left.')
else:
    print(f'Not enough money! You need {(expenses - budget):.2f} leva.')
