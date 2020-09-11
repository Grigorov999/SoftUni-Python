max_hp = 100
current_hp = max_hp
bit_coins = 0
amount_healed = 0
room_count = 0
game_over = False
tokens = []

room = input().split('|')
for element in room:
    tokens = element.split()
    room_count += 1
    if game_over == True:
        break

    if tokens[0] != 'potion' and tokens[0] != 'chest':
        monster = str(tokens[0])
        dmg = int(tokens[1])
        current_hp -= dmg
        if current_hp > 0:
            print(f'You slayed {monster}.')
        elif current_hp <= 0:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {room_count}')
            game_over = True

    elif tokens[0] == 'potion':
        heal = int(tokens[1])
        current_hp += heal
        amount_healed = (max_hp + heal) - (current_hp + heal)
        if current_hp > 100:
            current_hp = max_hp
        print(f'You healed for {amount_healed} hp.')
        print(f'Current health: {current_hp} hp.')

    elif tokens[0] == 'chest':
        coins = int(tokens[1])
        bit_coins += coins
        print(f'You found {coins} bitcoins.')

if game_over == False:
    print(f"You've made it!")
    print(f"Bitcoins: {bit_coins}")
    print(f"Health: {current_hp}")
