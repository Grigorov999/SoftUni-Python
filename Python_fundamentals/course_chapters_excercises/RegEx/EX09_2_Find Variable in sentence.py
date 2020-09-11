import re

text = input()

pattern = r"\b_[a-zA-Z0-9]+\b"

matches = re.findall(pattern, text)

print(','.join([i[1:] for i in matches]))
