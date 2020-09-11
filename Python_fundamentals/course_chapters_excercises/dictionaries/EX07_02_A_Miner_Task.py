# You will be given a sequence of strings, each on a new line. Every odd line on the console is representing a resource
# (e.g. Gold, Silver, Copper, and so on) and every even – quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} –> {quantity}


final_dict = {}

while True:
    command = input()
    if command == 'stop':
        break

    quantity = int(input())
    resource = command

    if resource not in final_dict:
        final_dict[resource] = quantity
    else:
        final_dict[resource] += quantity

for r in final_dict:
    print(f"{r} -> {final_dict[r]}")
