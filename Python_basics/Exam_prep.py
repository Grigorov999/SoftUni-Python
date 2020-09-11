poor_grades_allowed = int(input())

task_name = str
task_grade = int
has_failed = True
solved_problems_count = 0
failed_times = 0
grades_sum = 0
last_problem = str

while failed_times < poor_grades_allowed:
    task_name = input()
    if task_name == 'Enough':
        has_failed = False
        break

    task_grade = int(input())
    if task_grade <= 4:
        failed_times += 1
    grades_sum += task_grade
    solved_problems_count += 1
    last_problem = task_name

if has_failed:
    print(f'You need a break, {poor_grades_allowed} poor grades.')
else:
    print(f'Average score: {grades_sum / solved_problems_count:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')
