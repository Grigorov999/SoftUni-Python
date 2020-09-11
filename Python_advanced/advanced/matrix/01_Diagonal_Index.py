def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


n = int(input())
matrix = []

for _ in range(n):
    matrix.append(read_int_list_from_input())

main_diagonal_sum = 0
secondary_diagonal_sum = 0
difference = 0

for i in range(len(matrix)):
    main_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][(n-1)-i]

difference = abs(main_diagonal_sum - secondary_diagonal_sum)

print(difference)
