n = int(input())

presentation = input()
total_sum = 0
counter = 0
while presentation != "Finish":
    current_sum = 0

    for i in range(1, n + 1):
        grade = float(input())
        current_sum += grade

    average_grade = current_sum / n
    total_sum += average_grade
    print(f'{presentation} - {average_grade:.2f}.')
    counter += 1
    presentation = input()

print(f"Student\'s final assessment is {(total_sum / counter):.2f}.")
