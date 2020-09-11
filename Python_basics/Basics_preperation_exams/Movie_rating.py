import sys

average_rating = 0
max_rating = -sys.maxsize
min_rating = sys.maxsize
rating_sum = 0
best_movie = ''
worst_movie = ''

movie_count = int(input())
for i in range(1, movie_count+1):
    movie_name = input()
    rating = float(input())

    rating_sum += rating

    if rating > max_rating:
        max_rating = rating
        best_movie = movie_name

    if rating < min_rating:
        min_rating = rating
        worst_movie = movie_name

average_rating = rating_sum / movie_count

print(f'{best_movie} is with highest rating: {max_rating}')
print(f'{worst_movie} is with lowest rating: {min_rating}')
print(f'Average rating: {average_rating:.1f}')
