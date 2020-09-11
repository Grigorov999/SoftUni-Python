l = int(input())
w = int(input())
h = int(input())
ocps = float(input())

v = l * w * h
full_tank = v * 0.001

perc = ocps * 0.01

aquarium = full_tank * ( 1 - perc)

print(f'{aquarium:.3f}')
