age_lili = int(input())
price_washing_machine = float(input())
price_toy = int(input())

birth_day_count = age_lili

count_toys = 0
gift_money = 0
brother_take = 0


for i in range(1, birth_day_count+1):
    if i % 2 == 0:
        gift_money += i / 2 * 10
        brother_take += 1

    else:
        count_toys += 1

toy_total_p = count_toys * price_toy
savings_total = ((gift_money + toy_total_p) - brother_take)
n = savings_total - price_washing_machine
m = price_washing_machine - savings_total

if savings_total >= price_washing_machine:
    print(f'Yes! {n:.2f}')
else:
    print(f'No! {m:.2f}')
