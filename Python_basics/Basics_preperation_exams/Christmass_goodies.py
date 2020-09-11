budget = int(input())

command = input()
while command != 'Stop':
    current_price = 0

    for letter in command:
        current_price += ord(letter)

    if budget >= current_price:
        budget -= current_price
        print('Item successfully purchased!')
    else:
        budget -= current_price
        print('Not enough money!')
        break
    command = input()

if budget >= 0:
    print(f'Money left: {budget}')
