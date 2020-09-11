def factorial(n):
    for i in range(n, 1, -1):
        n = n * (i - 1)
    return n


a = int(input())
b = int(input())

result = factorial(a) / factorial(b)

print(f"{result:.2f}")
