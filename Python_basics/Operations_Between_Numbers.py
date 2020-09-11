N1 = int(input())
N2 = int(input())
operator = input()

result1 = 0
result2 = 0.00
mod = 0

if operator == '+':
    result1 = N1 + N2
    if result1 % 2 == 0:
        print(f'{N1} {operator} {N2} = {result1} - even')
    else:
        print(f'{N1} {operator} {N2} = {result1} - odd')
elif operator == '-':
    result1 = N1 - N2
    if result1 % 2 == 0:
        print(f'{N1} {operator} {N2} = {result1} - even')
    else:
        print(f'{N1} {operator} {N2} = {result1} - odd')
elif operator == '*':
    result1 = N1 * N2
    if result1 % 2 == 0:
        print(f'{N1} {operator} {N2} = {result1} - even')
    else:
        print(f'{N1} {operator} {N2} = {result1} - odd')
elif operator == '/':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result2 = N1 / N2
        print(f'{N1} {operator} {N2} = {result2:.2f}')
elif operator == '%':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        mod = N1 % N2
        print(f'{N1} {operator} {N2} = {mod}')

