number = int(input())
empty_stack = []

for _ in range(number):
    command = list(map(int, input().split(" ")))
    token = command[0]

    if token == 1:
        item = command[1]
        empty_stack.append(item)
    if empty_stack:
        if token == 2:
            empty_stack.pop()
        elif token == 3:
            print(max(empty_stack))
        elif token == 4:
            print(min(empty_stack))

print(", ".join([str(x) for x in reversed(empty_stack)]))
