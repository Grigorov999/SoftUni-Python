baklava_price = float(input())
muffin_price = float(input())
kg_stohlen = float(input())
kg_candy = float(input())
kg_coockies = int(input())

stohlen_price = baklava_price + (baklava_price * 0.6)
sum_stohlen = kg_stohlen * stohlen_price

candy_price = muffin_price + (muffin_price * 0.8)
sum_candy = candy_price * kg_candy

coockies_price = 7.50
sum_coockies = kg_coockies * coockies_price

final_sum_needed = sum_stohlen + sum_candy + sum_coockies
print(f'{final_sum_needed:.2f}')