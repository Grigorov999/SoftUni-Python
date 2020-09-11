usernames = input().split(", ")

counter = 0

for username in usernames:
    if 3 <= len(username) <= 16:

        for ch in username:
            if ch.isalnum():
                counter += 1
            elif ch == "-":
                counter += 1
            elif ch == "_":
                counter += 1

        if counter == len(username):
            print(username)
            counter = 0
        counter = 0
