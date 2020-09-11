n = int(input())
sum_count1 = 0
sum_count2 = 0
sum_count3 = 0
sum_count4 = 0
sum_count5 = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        sum_count1 += 1
        p1 = sum_count1 / n * 100

    elif 200 <= num <= 399:
        sum_count2 += 1
        p2 = sum_count2 / n * 100

    elif 400 <= num <= 599:
        sum_count3 += 1
        p3 = sum_count3 / n * 100

    elif 600 <= num <= 799:
        sum_count4 += 1
        p4 = sum_count4 / n * 100

    elif 800 <= num <= 1000:
        sum_count5 += 1
        p5 = sum_count5 / n * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
