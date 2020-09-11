Whiskey_Price = float(input())
Beer_Quantity = float(input())
Wine_Quantity = float(input())
Rakia_Quantity = float(input())
Whiskey_Quantity = float(input())

Rakia_Price = Whiskey_Price / 2
Wine_Price = Rakia_Price - (0.4 * Rakia_Price)
Beer_Price = Rakia_Price - (0.8 * Rakia_Price)

Rakia = Rakia_Quantity * Rakia_Price
Wine = Wine_Quantity * Wine_Price
Beer = Beer_Quantity * Beer_Price
Whiskey = Whiskey_Price * Whiskey_Quantity

Sum = Whiskey + Rakia + Wine + Beer
print(f'{Sum:.2f}')

