passengers_count = int(input())
bus_stops = int(input())

for i in range(1, bus_stops+1):
    count_off = int(input())
    count_on = int(input())
    passengers_count -= count_off
    passengers_count += count_on

    if i % 2 == 1:
        passengers_count += 2
    else:
        passengers_count -= 2

print(f'The final number of passengers is : {passengers_count}')
