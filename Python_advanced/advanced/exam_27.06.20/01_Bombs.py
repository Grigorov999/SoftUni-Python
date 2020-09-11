from collections import deque

first_bomb_effect = deque(map(int, input().split(',')))
last_bomb_casing = list(map(int, input().split(',')))

bombs_dict = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}

crafted_bombs = []

Datura_Bombs = 0
Cherry_Bombs = 0
Smoke_Decoy_Bombs = 0


while first_bomb_effect and last_bomb_casing:
    if Datura_Bombs >= 3 and Cherry_Bombs >= 3 and Smoke_Decoy_Bombs >= 3:
        break

    first_substring = first_bomb_effect.popleft()
    last_substring = last_bomb_casing.pop()
    combination = first_substring + last_substring

    if combination not in bombs_dict.values():
        last_substring -= 5
        last_bomb_casing.append(last_substring)
        first_bomb_effect.appendleft(first_substring)

    if combination in bombs_dict.values():
        if combination == 40:
            Datura_Bombs += 1
        elif combination == 60:
            Cherry_Bombs += 1
        elif combination == 120:
            Smoke_Decoy_Bombs += 1

if Datura_Bombs >= 3 and Cherry_Bombs >= 3 and Smoke_Decoy_Bombs >= 3:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')

if len(first_bomb_effect) == 0:
    print('Bomb Effects: empty')
else:
    pre_print_1 = ", ".join([str(x) for x in first_bomb_effect])
    print(f'Bomb Effects: {pre_print_1}')
if len(last_bomb_casing) == 0:
    print('Bomb Casings: empty')
else:
    pre_print_2 = ", ".join([str(y) for y in last_bomb_casing])
    print(f'Bomb Casings: {pre_print_2}')

print(f'Cherry Bombs: {Cherry_Bombs}')
print(f'Datura Bombs: {Datura_Bombs}')
print(f'Smoke Decoy Bombs: {Smoke_Decoy_Bombs}')
