import math

w = float(input())
l = float(input())
h = float(input())
astronaut_average_height = float(input())

V_space_ship = w * l * h
V_room = (astronaut_average_height + 0.40) * 2 * 2
astronaut_count = math.floor(V_space_ship / V_room)

if 3 <= astronaut_count <= 10:
    print(f'The spacecraft holds {astronaut_count} astronauts.')
elif astronaut_count < 3:
    print('The spacecraft is too small.')
else:
    print('The spacecraft is too big.')
