n = int(input())
capacity = 255
counter = 0

for i in range(0, n):
    litters = int(input())
    if (counter + litters) > capacity:
        print(f'Insufficient capacity!')
    else:
        counter += litters

print(counter)
