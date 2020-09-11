result_dict = {}
input_string = input()

for char in input_string:
    if char != " ":
        if char not in result_dict:
            result_dict[char] = 1
        else:
            result_dict[char] += 1

for c in result_dict:
    print(f'{c} -> {result_dict[c]}')
