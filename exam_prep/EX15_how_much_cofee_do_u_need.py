command = ''
counter = 0
sum = 0
while command != 'END':
    if command == 'END':
        break

    command = str(input())
    counter += 1
    if ["dog", "cat", "movie", "coding"]:
        if command.isupper():
            sum += 2
        elif command.islower():
            sum += 1

    if counter == 5:
        print('You need extra sleep')
        break
    command = str(input())

print(sum)
