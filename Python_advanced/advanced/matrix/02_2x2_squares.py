rows, cols = map(int, input().split(' '))
matrix = [input().split(' ') for _ in range(rows)]

result = 0

for row in range(rows - 1):
    for element in range(cols - 1):
        if matrix[row][element] == matrix[row][element + 1] == matrix[row + 1][element] == matrix[row + 1][element + 1]:
            result += 1

print(result)
