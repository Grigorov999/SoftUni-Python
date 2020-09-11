flower_type = (input())
flower_count = int(input())
budget = int(input())

price = 0.0
dsc = 0.0

if flower_type == "Roses":
    if flower_count <= 80:
        price = flower_count * 5
    else:
        dsc = 0.10 * flower_count
        price = (flower_count * 5) - dsc

elif flower_type == "Dahlias":
    if flower_count <= 90:
        price = flower_count * 3.80
    else:
        dsc = 0.15 * flower_count
        price = (flower_count * 3.80) - dsc

elif flower_type == "Tulips":
    if flower_count <= 80:
        price = flower_count * 2.80
    else:
        dsc = 0.15 * flower_count
        price = (flower_count * 2.80) - dsc

if flower_type == "Narcissus":
    if flower_count >= 120:
        price = flower_count * 3.00
    else:
        dsc = 0.15 * flower_count
        price = (flower_count * 3.00) + dsc

if flower_type == "Gladiolus":
    if flower_count >= 80:
        price = flower_count * 2.00
    else:
        dsc = 0.2 * flower_count
        price = (flower_count * 2.00) + dsc

if budget >= price:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {(budget - price):.2f} leva left.')
else:
    print(f"Not enough money, you need {(price - budget):.2f} leva more.")
