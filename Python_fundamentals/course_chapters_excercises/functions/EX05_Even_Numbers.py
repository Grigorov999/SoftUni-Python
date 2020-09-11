num = list(map(lambda x: int(x), input().split(', ')))
even = []

for i in range(len(num)):
    if num[i] % 2 == 0:
        even.append(i)

print(even)
