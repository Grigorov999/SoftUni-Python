user_name = input()
correct_password = input()

password = input()
while password != correct_password:
    password = input()

print(f'Welcome {user_name}!')