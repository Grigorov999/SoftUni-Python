destination = input()
sum_needed = 0.0

while destination != 'End':
    if destination == 'End':
        break
    sum_needed = float(input())
    sum_savings = 0.0
    while sum_savings <= sum_needed:
        savings = float(input())
        sum_savings += savings

    print(f'Going to {destination}!')
    destination = input()
