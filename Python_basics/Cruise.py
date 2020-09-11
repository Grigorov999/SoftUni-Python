budget = float(input())
season = input()

destination = str
spend = 0.00
vacation_type = str

if budget <= 100.00:
    destination = 'Somewhere in Bulgaria'
    if season == 'summer':
        spend = budget * 0.30
        vacation_type = 'Camp'
    else:
        spend = budget * 0.70
        vacation_type = 'Hotel'
elif 101 <= budget <= 1000:
    destination = 'Somewhere in Balkans'
    if season == 'summer':
        spend = budget * 0.40
        vacation_type = 'Camp'
    else:
        spend = budget * 0.80
        vacation_type = 'Hotel'
else:
    destination = 'Somewhere in Europe'
    spend = budget * 0.90
    vacation_type = 'Hotel'

print(destination)
print(f'{vacation_type} - {spend:.2f}')
