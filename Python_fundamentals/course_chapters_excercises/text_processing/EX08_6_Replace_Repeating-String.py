text = input()

output_text = []

for i in range(len(text)):
    if i < len(text) - 1:
        if text[i] == text[i + 1]:
            continue
        else:
            output_text.append(text[i])
    else:
        output_text.append(text[i])

print("".join(output_text))
