n = int(input())
counter1 = 0
counter2 = 0
for i in range(n):
    line = str(input())
    if line == '(':
        counter1 += 1
    elif line == ')':
        counter2 += 1
        if counter1 - counter2 != 0:
            print(f'UNBALANCED')

if counter1 == counter2:
    print(f'BALANCED')
else:
    print(f'UNBALANCED')
