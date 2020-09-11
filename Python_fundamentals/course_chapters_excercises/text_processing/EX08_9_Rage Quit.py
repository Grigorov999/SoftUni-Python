line = input()

letters = ''
result = ''

for i in range(len(line)):
    if line[i].isnumeric():
        factor = line[i]
        digit = i + 1
        while digit < len(line) and line[digit].isnumeric():
            factor += line[digit]
            digit += 1

        letters = letters.upper() * int(factor)
        result += letters
        letters = ''

    else:
        letters += line[i]

print(f"Unique symbols used: {len(set(result))}")
print(result)
