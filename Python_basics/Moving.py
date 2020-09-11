width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

volume_taken = 0

while volume_taken < volume:
    input_text = input()
    if input_text == 'Done':
        print(f'{volume - volume_taken} Cubic meters left.')
        break

    boxes_count = int(input_text)
    needed_volume = boxes_count
    boxes_count += needed_volume

if volume_taken > volume:
    print(f'No more free space! You need {volume_taken - volume} Cubic meters more.')

