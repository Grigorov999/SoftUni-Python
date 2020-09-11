money_needed = float(input())
money_available = float(input())

counter_days = 0
counter_spend = 0

while money_available < money_needed and counter_spend < 5:
    action = input()
    money = float(input())
    counter_days += 1
    if action == 'save':
        money_available += money
        counter_spend += 0
    elif action == 'spend':
        money_available -= money
        counter_spend += 1
        if money_available < 0:
            money_available = 0

if counter_spend == 5:
    print('You can\'t save the money.')
    print(f'{counter_days:.0f}')

if money_available >= money_needed:
    print(f'You saved the money for {counter_days:.0f} days.')
