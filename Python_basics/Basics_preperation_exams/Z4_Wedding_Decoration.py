price = 0.0
current_budget = 0.0

budget = float(input())
command = input()
while command != 'stop':
    if command == 'stop' or budget < 0.0:
        break

    if command == 'balloons':
        goods_count = int(input())
        price = goods_count * 0.10
    elif command == 'flowers':
        goods_count = int(input())
        price = goods_count * 1.50
    elif command == 'candles':
        goods_count = int(input())
        price = goods_count * 0.50
    elif command == 'ribbon':
        goods_count = int(input())
        price = goods_count * 2

    price += price
    budget -= price

    command = input()

if command == 'stop':
    print(f'Spend money: {price}')
    print(f'Money left: {(budget - price):.2f}')

if budget < 0.0:
    print(f'All money is spent!')

