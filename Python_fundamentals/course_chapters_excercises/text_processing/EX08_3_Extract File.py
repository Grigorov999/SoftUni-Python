string_line = input().split('\\')

name, extension = string_line[-1].split('.')

print(f'File name: {str(name)}')
print(f'File extension: {str(extension)}')
