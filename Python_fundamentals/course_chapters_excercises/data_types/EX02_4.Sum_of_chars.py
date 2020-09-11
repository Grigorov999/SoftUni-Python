num = int(input())

total_sum = 0

for i in range(0, num):
    char_input = input()
    total_sum += ord(char_input)

print(f'The sum equals: {total_sum}')
