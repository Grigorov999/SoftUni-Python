steps = 0
tenk = 10000

while steps < tenk:
    action = input()
    if action == 'Going home':
        steps_home = int(input())
        steps += steps_home
        break

    else:
        current_steps = int(action)
        steps += current_steps

if steps >= tenk:
    print('Goal reached! Good job!')
else:
    print(f'{tenk - steps} more steps to reach goal.')
