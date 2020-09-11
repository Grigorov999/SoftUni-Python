food_money = float(input())
suvenier_money = float(input())
hotel_price = float(input())

gas_needed = 420 / 100 * 7
gas_budget = gas_needed * 1.85

daily_expenses = food_money * 3 + suvenier_money * 3

first_day_discount = hotel_price * 0.9
second_day_discount = hotel_price * 0.85
third_day_discount = hotel_price * 0.8

hotel_total = first_day_discount + second_day_discount + third_day_discount
total_money = gas_budget + daily_expenses + hotel_total

print(f'Money needed: {total_money:.2f}')
