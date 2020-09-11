width = int(input())
length = int(input())

cake_whole = width * length

pieces = 0

while pieces <= cake_whole:
    action = input()
    if action == 'STOP':
        print(f'{cake_whole - pieces} pieces are left.')
        break

    else:
        pieces += int(action)

    if pieces > cake_whole:
        print(f'No more cake left! You need {pieces - cake_whole} pieces more.')
