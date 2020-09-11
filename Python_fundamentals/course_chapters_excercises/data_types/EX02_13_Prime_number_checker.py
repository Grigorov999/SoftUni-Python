n = int(input())

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f'False')
            break

    else:
        print(f'True')
else:
    print(f'False')
