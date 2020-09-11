days = float(input())
coocks = float(input())
cakes = float(input())
goffretes = float(input())
pancakes = float(input())

CakeCost = cakes * 45
GoffretesCost = goffretes * 5.80
PancakesCost = pancakes * 3.20

SumForDay = (CakeCost + GoffretesCost + PancakesCost) * coocks
SumCampaign = SumForDay * days

SumAfterCost = SumCampaign - (1/8 * SumCampaign)
print(f'{SumAfterCost:.2f}')