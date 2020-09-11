n = int(input())
salary = int(input())

count1 = 0
count2 = 0
count3 = 0

deduction_facebook = 150
deduction_instagram = 100
deduction_reddit = 50

for i in range(n):
    tab = str(input())
    if salary != 0:
        if tab == 'Facebook':
            salary -= deduction_facebook
            if salary == 0:
                print(f'You have lost your salary.')
                break

        if tab == 'Instagram':
            salary -= deduction_instagram
            if salary == 0:
                print(f'You have lost your salary.')
                break

        if tab == 'Reddit':
            salary -= deduction_reddit
            if salary == 0:
                print(f'You have lost your salary.')
                break
if salary != 0:
    print(salary)
