n = int(input())

sum_odd = 0
sum_even = 0


for i in range(1, n+1):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
    elif i % 2 != 0:
        sum_odd += num

if sum_odd == sum_even:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    print('No')
    print(f'Diff = {abs(sum_odd - sum_even)}')
