import sys
entry_count = int(input())

total = 0
max_num = -sys.maxsize

for i in range(entry_count):
    num = int(input())
    total += num
    if num > max_num:
        max_num = num

total -= max_num

if total == max_num:
    print('Yes')
    print(f'Sum = {total}')
else:
    print('No')
    print(f'Diff = {abs(max_num - total)}')
