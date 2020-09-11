import math

hall_lenght = float(input())
hall_width = float(input())
bar_side = float(input())


hall_space = hall_lenght * hall_width
bar_space = bar_side * bar_side
dancing_space = hall_space * 0.19
free_space = hall_space - bar_space - dancing_space

guests_count = math.ceil(free_space / 3.2)

print(guests_count)
