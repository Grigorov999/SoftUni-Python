x = input()
y = x[len(x)-1:0:-1]+x[0]

num1 = y[0]
num2 = y[1]
num3 = y[2]

m = int(num1)
l = int(num2)
n = int(num3)

for i in range(1, m+1):
    for j in range(1, l+1):
        for k in range(1, n+1):
            result = i * j * k
            print(f'{i} * {j} * {k} = {result};')
