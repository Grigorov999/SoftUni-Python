def is_palindrome(n):
    if n == n[::-1]:
        return True
    return False


num = input().split(", ")

for n in num:
    print(is_palindrome(n))
