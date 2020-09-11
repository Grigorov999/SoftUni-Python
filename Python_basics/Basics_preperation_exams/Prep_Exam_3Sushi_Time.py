import math

sushi_type = input()
restourant = input()
orders_count = int(input())
to_go = input()

total_price = 0
invalid = False

if sushi_type == 'sashimi':
    if restourant == 'Sushi Zone':
        total_price = orders_count * 4.99
        invalid = True
    elif restourant == 'Sushi Time':
        total_price = orders_count * 5.49
        invalid = True
    elif restourant == 'Sushi Bar':
        total_price = orders_count * 5.25
        invalid = True
    elif restourant == 'Asian Pub':
        total_price = orders_count * 4.50
        invalid = True

elif sushi_type == 'maki':
    if restourant == 'Sushi Zone':
        total_price = orders_count * 5.29
        invalid = True
    elif restourant == 'Sushi Time':
        total_price = orders_count * 4.69
        invalid = True
    elif restourant == 'Sushi Bar':
        total_price = orders_count * 5.55
        invalid = True
    elif restourant == 'Asian Pub':
        total_price = orders_count * 4.80
        invalid = True

elif sushi_type == 'uramaki':
    if restourant == 'Sushi Zone':
        total_price = orders_count * 5.99
        invalid = True
    elif restourant == 'Sushi Time':
        total_price = orders_count * 4.49
        invalid = True
    elif restourant == 'Sushi Bar':
        total_price = orders_count * 6.25
        invalid = True
    elif restourant == 'Asian Pub':
        total_price = orders_count * 5.50
        invalid = True

elif sushi_type == 'temaki':
    if restourant == 'Sushi Zone':
        total_price = orders_count * 4.29
        invalid = True
    elif restourant == 'Sushi Time':
        total_price = orders_count * 5.19
        invalid = True
    elif restourant == 'Sushi Bar':
        total_price = orders_count * 4.75
        invalid = True
    elif restourant == 'Asian Pub':
        total_price = orders_count * 5.50
        invalid = True

if to_go == 'Y':
    delivery = total_price * 0.2
    total_price += delivery
elif to_go == 'N':
    total_price = total_price

if invalid == True:
    print(f'Total price: {math.ceil(total_price)} lv.')
else:
    print(f'{restourant} is invalid restaurant!')
