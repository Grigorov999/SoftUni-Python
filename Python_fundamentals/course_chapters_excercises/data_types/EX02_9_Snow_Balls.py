n = int(input())
maximum = 0
s = 0
t = 0
q = 0

for i in range(n):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())

    snowballValue = int((snowballSnow / snowballTime) ** snowballQuality)

    if snowballValue > maximum:
        maximum = snowballValue
        s = snowballSnow
        t = snowballTime
        q = snowballQuality

print(f'{s} : {t} = {maximum} ({q})')
