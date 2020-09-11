budget = float(input())
ski_price = float(input())
sticks_price = float(input())

total = 0
money_left = 0

ski_shoes_price = ski_price * 0.6

ski_clothes_price = (ski_price - (ski_price * 0.4)) + ski_shoes_price

current_cost = ski_price + ski_shoes_price + ski_clothes_price

if current_cost > 800:
    total = current_cost
    money_left = budget - total
elif current_cost <= 800:
    total = current_cost + sticks_price
    money_left = budget - total

if total <= budget:
    print(f'Angel\'s sum is {total:.2f} lv. He has {money_left:.2f} lv. left.')
else:
    print(f'Not enough money! You need {(total - budget):.2f} leva more!')
