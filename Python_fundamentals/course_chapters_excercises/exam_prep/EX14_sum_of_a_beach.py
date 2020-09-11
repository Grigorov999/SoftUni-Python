my_string = input()
p = sum(my_string.lower().count(word) for word in ["sand", "water", "fish", "sun"])
print(p)
