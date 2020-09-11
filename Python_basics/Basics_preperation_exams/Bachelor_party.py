total_guests = 0
income = 0

guest_singer = int(input())
command = input()
while command != 'The restaurant is full':
    num = int(command)

    if num < 5:
        income += num * 100
    elif num >= 5:
        income += num * 70

    total_guests += num
    command = input()

if income >= guest_singer:
   print(f'You have {total_guests} guests and {income - guest_singer} leva left.')
else:
    print(f'You have {total_guests} guests and {income} leva income, but no singer.')
