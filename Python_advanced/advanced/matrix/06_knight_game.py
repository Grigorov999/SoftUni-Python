def is_valid(pos, n):
    row = pos[0]
    col = pos[1]
    return 0 <= row < n and 0 <= col < n


def get_killed_knights(row, col, n, matrix):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, n) and matrix[current_pos[0]][current_pos[1]] == 'K':
            killed_knights += 1

    return killed_knights


n = int(input())
matrix = [list(input()) for _ in range(n)]
total_kills = 0

while True:

    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                killed_knights = get_killed_knights(row, col, n, matrix)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]

    if most_kills == 0:
        break

    matrix[to_kill[0]][to_kill[1]] = '0'
    total_kills += 1

print(total_kills)
