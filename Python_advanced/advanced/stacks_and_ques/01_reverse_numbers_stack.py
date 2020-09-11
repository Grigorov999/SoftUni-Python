n = [int(x) for x in input().split()]
element = [int(x) for x in n]
result = []

[result.append(element.pop()) for _ in range(len(element))]

print(' '.join([str(i) for i in result]))
