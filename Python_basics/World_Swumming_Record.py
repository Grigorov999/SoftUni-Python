record_per_sec = float(input())
range_meters = float(input())
time_per_second = float(input())

whole_time = range_meters * time_per_second
resistance = (range_meters // 15) * 12.5
end_time = whole_time + resistance

if record_per_sec <= end_time:
    print(f'No, he failed! He was {(end_time - record_per_sec):.2f} seconds slower.')
elif record_per_sec > end_time:
    print(f'Yes, he succeeded! The new world record is {end_time:.2f} seconds.')