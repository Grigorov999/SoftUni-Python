import math

p_count = int(input())
n_capacity = int(input())

elevator = math.ceil(p_count / n_capacity)

print(int(elevator))
