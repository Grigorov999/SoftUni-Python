
Price_Vacation = float(input())
Sold_Puzzle = int(input())
Sold_Doll = int(input())
Sold_Bear = int(input())
Sold_Minion = int(input())
Sold_Truck = int(input())

Total_Price = (Sold_Puzzle*2.60) + (Sold_Doll*3) + (Sold_Bear*4.10) + (Sold_Minion*8.20) + (Sold_Truck*2)
Total_Count = Sold_Puzzle + Sold_Doll + Sold_Bear + Sold_Minion + Sold_Truck

if Total_Count >= 50:
    Total_Price = Total_Price * (1 - 0.25)

Total_Price = Total_Price * (1 - 0.1)
Money = abs(Total_Price - Price_Vacation)

if Total_Price >= Price_Vacation:
    print(f'Yes! {abs(Money):.2f} lv left.')
else:
    print(f'Not enough money! {abs(Money):.2f} lv needed.')
