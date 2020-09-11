movie = (input())
row = int(input())
col = int(input())

cinema_capacity = row * col

if movie == 'Premiere':
    profit = cinema_capacity * 12.00
    print(profit)

elif movie == 'Normal':
    profit = cinema_capacity * 7.50
    print(profit)

elif movie == 'Discount':
    profit = cinema_capacity * 5.00
    print(profit)