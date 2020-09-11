final_dict = {}

while True:
    lines = input().split()
    if lines[0] == 'buy':
        break

    product = lines[0]
    price = float(lines[1])
    quantity = int(lines[2])

    if product not in final_dict:
        final_dict[product] = [price, quantity]
    else:
        final_dict[product][0] = price
        final_dict[product][1] += quantity

for (key, val) in final_dict.items():
    total_price = val[0] * val[1]
    print(f'{key} -> {total_price:.2f}')

