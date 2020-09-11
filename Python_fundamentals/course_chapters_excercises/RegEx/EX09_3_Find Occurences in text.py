import re

text = input().lower()
target_word = input().lower()

pattern = f"\\b{target_word}\\b"

matches = re.findall(pattern, text)

print(len(matches))
