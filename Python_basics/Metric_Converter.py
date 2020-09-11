value = float(input())
in_metric = str(input())
out_metric = str(input())

if in_metric == 'mm':
    value /= 1000
elif in_metric == 'cm':
    value /= 100

if out_metric == 'mm':
    value *= 1000
elif out_metric == 'cm':
    value *= 100

print(f'{value:.3f}')
