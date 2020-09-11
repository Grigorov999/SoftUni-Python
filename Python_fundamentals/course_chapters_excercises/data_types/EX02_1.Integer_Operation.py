import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

multy = a + b
divide = int(math.floor(multy / c))
end_res = int(math.floor(divide * d))

print(int(end_res))
