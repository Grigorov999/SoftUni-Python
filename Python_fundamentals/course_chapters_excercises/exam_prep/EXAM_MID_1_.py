import math

student_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

total_bonus = 0
max_bonus = 0
best_student = 0

for i in range(student_count):
    attendances = int(input())
    total_bonus = attendances / lectures_count * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        best_student = attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {best_student} lectures.')
