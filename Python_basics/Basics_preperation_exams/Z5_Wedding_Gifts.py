total_guests = int(input())
gift_count = int(input())

count1 = 0
count2 = 0
count3 = 0
count4 = 0

percent1 = 0
percent2 = 0
percent3 = 0
percent4 = 0

total_gifts_percent = 0

for i in range(1, gift_count+1):
    type = input()

    if type == 'A':
        count1 += 1
    if type == 'B':
        count2 += 1
    if type == 'V':
        count3 += 1
    if type == 'G':
        count4 += 1

percent1 = count1 / gift_count * 100
percent2 = count2 / gift_count * 100
percent3 = count3 / gift_count * 100
percent4 = count4 / gift_count * 100

total_gifts_percent = gift_count / total_guests * 100

print(f'{percent1:.2f}%')
print(f'{percent2:.2f}%')
print(f'{percent3:.2f}%')
print(f'{percent4:.2f}%')
print(f'{total_gifts_percent:.2f}%')
