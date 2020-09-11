student_name = input()

grades_counter = 1
grades_sum = 0
current_grade_final = 0.00
average_mark = 0.00

while grades_counter <= 12:
    current_grade_final = float(input())
    if current_grade_final >= 4:
        grades_counter += 1
        grades_sum += current_grade_final
        average_mark = grades_sum / 12
    else:
        print(f'{student_name} has been excluded at {grades_counter} grade')
        break

if current_grade_final >= 4:
    print(f'{student_name} graduated. Average grade: {average_mark:.2f}')
