first_num = int(input())
second_num = int(input())
magic_number = int(input())

position = 0
is_found = False

for i in range(first_num, second_num+1):
    if is_found:
       break

    for j in range(first_num, second_num+1):
        position += 1
        if i + j == magic_number:
            if position != 0:
                print(f'Combination N:{position} ({i} + {j} = {magic_number})')
                is_found = True

if not is_found:
    print(f'{position} combinations - neither equals {magic_number}')
