def calculate_below_primary_diagonal(matrix):
    n = len(matrix)
    final_sum = 0
    for row in range(n):
        for col in range(row + 1):
            final_sum += matrix[row][col]
    return final_sum


def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


n = int(input())
matrix = []

for _ in range(n):
    matrix.append(read_int_list_from_input())


def find_symbol(matrix, symbol):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == symbol:
                return (row, col)

    return None


