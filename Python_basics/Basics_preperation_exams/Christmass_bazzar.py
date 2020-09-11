import math

target_sum_needed = float(input())
fantasy_books = int(input())
horror_books = int(input())
romance_books = int(input())

fantasy_price = 14.90
horror_price = 9.80
romance_price = 4.30

money_from_selling = (fantasy_books * fantasy_price) + (horror_books * horror_price) + (romance_books * romance_price)
VAT = money_from_selling * 0.2

profit = money_from_selling - VAT

if profit > target_sum_needed:
    remainder = profit - target_sum_needed
    sellers_gain = int(math.floor(remainder * 0.1))
    total = target_sum_needed + (remainder - sellers_gain)
    print(f'{total:.2f} leva donated.')
    print(f'Sellers will receive {sellers_gain} leva.')
else:
    money_needed = target_sum_needed - profit
    print(f'{money_needed:.2f} money needed.')
