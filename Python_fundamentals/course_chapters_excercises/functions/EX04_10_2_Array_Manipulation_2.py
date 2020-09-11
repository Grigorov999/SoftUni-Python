import sys


def read_number_arr():
    input_arr = input().split()

    nums = []
    for i in input_arr:
        nums.append(int(i))

    return nums


def exchange(nums, index):
    new_list = []

    for i in range(index+1, len(nums)):
        new_list.append(nums[i])

    for i in range(index+1):
        new_list.append(nums[i])

    return new_list


def max_number_index(nums, type):
    max_num = -sys.maxsize
    max_num_index = -1
    if type == 'even':
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0 and num >= max_num:
                max_num = num
                max_num_index = i
    else:
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0 and num >= max_num:
                max_num = num
                max_num_index = i

    return max_num_index(num)


def min_number_index(nums, type):
    min_num = sys.maxsize
    min_num_index = -1
    if type == 'even':
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0 and num <= min_num:
                min_num = num
                min_num_index = i
    else:
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0 and num <= min_num:
                min_num = num
                min_num_index = i

    return min_num_index(num)


def first_elements(nums, count, type):
    elements = []
    if type == 'even':
        for num in nums:
            if num % 2 == 0 and len(elements) < count:
                elements.append(num)

    else:
        for num in nums:
            if num % 2 != 0 and len(elements) < count:
                elements.append(num)

    return elements


def solve():
    nums = read_number_arr()

    command_input = input()
    while command_input != 'End':
        args = command_input.split()
        command_input = args[0]

        if command_input == 'exchange':
            index = int(args[1])

            if index < 0 or index >= len(nums):
                print('Invalid index')
                command_input = input()
                continue

            exchange(nums, index)
        elif command_input == 'max':
            type = args[1]
            max_index = max_number_index(nums, type)

            if max_index != -1:
                print(max_index)
            else:
                print('No matches')
        elif command_input == 'min':
            type = args[1]
            min_index = min_number_index(nums, type)

            if min_index != -1:
                print(min_index)
            else:
                print('No matches')
        elif command_input == 'first':
            count = int(args[1])
            type = args[2]

            if count > len(nums):
                print('Invalid count')
                command_input = input()
                continue

            print(first_elements(nums, count, type))

        command_input = input()


solve()
