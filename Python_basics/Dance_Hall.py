l = float(input())
w = float(input())
a = float(input())

Hall = (l * 100) * (w * 100)
Wardrobe = (a * 100) * (a * 100)
Bench = Hall / 10

FreeSpace = Hall - Wardrobe - Bench
import math
DancersCount = math.floor((FreeSpace / (40 + 7000)))

print(DancersCount)