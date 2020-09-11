import cmath

r = float(input())
pi = cmath.pi

area = pi * r ** 2
perimeter = 2 * pi * r

print(f'{area:.2f}')
print(f'{perimeter:.2f}')
