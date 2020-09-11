def is_palindrome(word):
    return word == word[::-1]


line = input().split()
searched = input()
palindrome = [word for word in line if is_palindrome(word)]

print(palindrome)
print(f'Found palindrome {palindrome.count(searched)} times')
