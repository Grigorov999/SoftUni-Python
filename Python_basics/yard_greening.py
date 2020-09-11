yards = float(input())

p = yards * 7.61
disc = 0.18 * p

fp = p - disc

print(f'The final price is: {fp:.2f} lv.')
print(f'The discount is: {disc:.2f} lv.')