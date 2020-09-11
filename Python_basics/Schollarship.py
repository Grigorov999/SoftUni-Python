import math

incom_in_leva = float(input())
average_grade = float(input())
minimum_wage = float(input())

social_scholarship = minimum_wage * 0.35
excellent_schollarship = average_grade * 25

if incom_in_leva < minimum_wage and average_grade > 4.50:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")

elif average_grade >= 5.50:
    print(f"You get a scholarship for excellent results {math.floor(excellent_schollarship)} BGN")

elif (incom_in_leva < minimum_wage and average_grade > 4.50) and (average_grade >= 5.50):

    if social_scholarship > excellent_schollarship:
        print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")

    elif social_scholarship < excellent_schollarship or social_scholarship == excellent_schollarship:
        print(f"You get a scholarship for excellent results {math.floor(excellent_schollarship)} BGN")

else:
    print("You cannot get a scholarship!")

