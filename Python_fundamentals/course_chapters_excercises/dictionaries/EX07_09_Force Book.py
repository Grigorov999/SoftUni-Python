force_book = {}

side = None
user = None

while True:
    input_string = input()
    if input_string == "Lumpawaroo":
        break

    if " | " in input_string:
        side, user = input_string.split(" | ")
        if side not in force_book:
            force_book[side] = []
        if user not in force_book[side]:
            force_book[side].append(user)
# 1. check and split 2. create list if valid  3. append list in dict if valid

    elif " -> " in input_string:
        user, side = input_string.split(" -> ")
        if side not in force_book:
            force_book[side] = []
        for dict_side in force_book:
            if user in force_book[dict_side]:
                force_book[dict_side].remove(user)
                if len(force_book[dict_side]) == 0:
                    del force_book[dict_side]
                    break

        force_book[side].append(user)
        print(f"{user} joins the {side} side!")

# 1. check and split 2. create list if valid  3. append list in dict if valid
# 4. if name exist - del  - append again with new side   5. print if valid

for side, users in sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(user) >= 1:
        print(f"Side: {side}, Members: {len(users)}")
        [print(f"! {name}") for name in sorted(users)]

#print each force side, ordered descending by forceUsers count, than ordered by name.
# For each side print the forceUsers,
# ordered by name.
#In case there are no forceUsers in a side, you shouldn`t print the side information.
