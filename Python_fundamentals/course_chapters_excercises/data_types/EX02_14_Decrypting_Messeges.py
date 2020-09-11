key = int(input())
n = int(input())
res = ''

for i in range(n):
    line = input()
    sym = key + ord(line)
    res += chr(sym)

print(res)
