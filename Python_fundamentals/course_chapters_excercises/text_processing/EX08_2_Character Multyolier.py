args = input().split()

word_one = args[0]
word_two = args[1]

min_len = min(len(word_one), len(word_two))
total_sum = 0

for i in range(min_len):
    total_sum += ord(word_one[i]) * ord(word_two[i])

long_word = word_one
if len(word_two) > len(word_one):
    long_word = word_two

for index in range(min_len, len(long_word)):
    total_sum += ord(long_word[index])

print(total_sum)
