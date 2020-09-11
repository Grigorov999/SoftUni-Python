items = input().split(', ')

command = input()
while command != 'Craft!':
    tokens = command.split(' - ')

    if tokens[0] == 'Collect':
        if tokens[1] not in items:
            items.append(tokens[1])

    if tokens[0] == 'Drop':
        if tokens[1] in items:
            items.remove(tokens[1])

    if tokens[0] == 'Combine Items':
        combination = tokens[1].split(':')
        if combination[0] in items:
            items.insert(0, combination[1])



    command = input()

print(", ".join(items))
