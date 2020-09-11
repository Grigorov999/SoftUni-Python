TableCount = float(input())
TableLenght = float(input())
TableWidt = float(input())

TableClothArea = TableCount * ((TableLenght + 2 * 0.30) * (TableWidt + 2 * 0.30))
TablePiesceArea = TableCount * (TableLenght / 2) * (TableLenght / 2)

PriceUSD = TableClothArea * 7 + TablePiesceArea * 9
PriceBGN = PriceUSD * 1.85

print(f'{PriceUSD:.2f} USD')
print(f'{PriceBGN:.2f} BGN')