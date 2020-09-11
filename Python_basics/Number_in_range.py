number = int(input())

while number < 1 or number > 100:
    print('Invalid number !')
    number = int(input())

print(f'Number is: {number}')
