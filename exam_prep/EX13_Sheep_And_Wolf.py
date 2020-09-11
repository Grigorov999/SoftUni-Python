line = input()
line = line.split(", ")
sheep_number = 0

if line[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in line:
        if i == "wolf":
            sheep_number = len(line) - (line.index("wolf")) - 1

    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
