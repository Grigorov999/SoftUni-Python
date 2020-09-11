string_line = input()
result_str = ''

for i in string_line:
    result_str += str(chr(ord(i)+3))

print(result_str)
