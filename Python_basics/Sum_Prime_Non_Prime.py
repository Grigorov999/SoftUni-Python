number = input()

prime_num = 0
non_prime_num = 0

while number != 'stop':
    number = int(input())
    if number < 0:
        print('Number is negative.')
    elif number == 0 or number == 1:
        non_prime_num += number
    elif number == 2:
        prime_num += number
    else:
        is_not_prime = False
        i = 0
        for i in range(2, i < number, i+1):
            if number % i == 0:
                non_prime_num += number
                is_not_prime = True
                break
        if not is_not_prime:
            prime_num += number

    number = input()
print(f'Sum of all prime numbers is: {prime_num}')
print(f'Sum of all non prime numbers is: {non_prime_num}')
