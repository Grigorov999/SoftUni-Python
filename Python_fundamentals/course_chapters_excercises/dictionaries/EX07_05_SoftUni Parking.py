n = int(input())
final_dict = {}

for i in range(n):
    command = input().split(' ')

    if command[0] == 'register':
        user_name = command[1]
        license_plate = command[2]
        if user_name not in final_dict:
            final_dict[user_name] = license_plate
            print(f'{user_name} registered {license_plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {license_plate}')

    if command[0] == 'unregister':
        user_name = command[1]
        if user_name not in final_dict:
            print(f'ERROR: user {user_name} not found')
        else:
            del final_dict[user_name]
            print(f"{user_name} unregistered successfully")

for j in final_dict:
    print(f"{j} => {final_dict[j]}")
