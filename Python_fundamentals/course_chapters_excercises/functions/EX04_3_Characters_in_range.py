def ascii_chars(a, b):
    for i in range(ord(a)+1, ord(b)):
        print(chr(i), end=' ')


a = input()
b = input()

ascii_chars(a, b)
