hour = int(input())
minutes = int(input())

time = hour * 60 + minutes
future_time = time + 15

result_hour = future_time // 60
result_minutes = future_time % 60

if result_hour > 23:
    result_hour -= 24

if result_minutes < 10:
    print(f'{result_hour}:0{result_minutes}')
else:
    print(f'{result_hour}:{result_minutes}')
