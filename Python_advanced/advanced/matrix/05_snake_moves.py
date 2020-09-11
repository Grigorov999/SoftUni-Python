from collections import deque

row, col = map(int, input().split())
snake = deque(input())

matrix = []

for row in range(row):
    current_list = []
    for element in range(col):
        part = snake.popleft()
        current_list.append(part)
        snake.append(part)

        if row % 2 != 0:
            if element == col-1:
                current_list = current_list[::-1]

    matrix.append(current_list)
    print(''.join(matrix[row]))
