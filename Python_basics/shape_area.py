import math

Write_Line = str(input()).lower()
area = 0.0

if Write_Line == 'square':
    a = float(input())
    area = a * a
    print(f'{area:.3f}')

elif Write_Line == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')

elif Write_Line == 'circle':
    a = float(input())
    area = (a ** 2) * math.pi
    print(f'{area:.3f}')

elif Write_Line == 'triangle':
    h = float(input())
    b = float(input())
    area = (h*b) / 2
    print(f'{area:.3f}')

