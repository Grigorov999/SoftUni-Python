grid_list = []
destroyed = 0

rows = int(input())

for row in range(rows):
    nums = list(map(int, input().split()))
    grid_list.append(nums)

attacks = input().split()

for attack in attacks:
    row, col = attack.split("-")
    row, col = int(row), int(col)

    if grid_list[row][col] != 0:
        grid_list[row][col] -= 1

        if grid_list[row][col] == 0:
            destroyed += 1

print(destroyed)
