x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs (x1 - x2)
widt = abs (y1 - y2)

area = length * widt
perimeter = 2 * length + 2 * widt

print(f'{area:.2f}')
print(f'{perimeter:.2f}')