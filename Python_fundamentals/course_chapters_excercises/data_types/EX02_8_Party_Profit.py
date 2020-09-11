import math

party_size = int(input())
days = int(input())
coins = 0
companions = party_size

for i in range(1, days+1):

    if i % 10 == 0:
        companions -= 2
    if i % 15 == 0:
        companions += 5

    coins += 50
    coins -= (2 * companions)

    if i % 3 == 0:
        coins -= (3 * companions)
    if i % 5 == 0:
        coins += (20 * companions)
        if i % 3 == 0:
            coins -= (2 * companions)

coins_each = coins / companions
print(f'{companions} companions received {math.floor(coins_each)} coins each.')
