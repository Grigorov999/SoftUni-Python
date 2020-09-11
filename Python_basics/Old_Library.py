book_name = input()
books_count = int(input())

counter = 0
book_found = False

while counter < books_count:
    current_book = input()
    if current_book == book_name:
        book_found = True
        print(f'You checked {counter} books and found it.')
        break

    counter += 1

if not book_found:
    print(f'The book you search is not here!')
    print(f'You checked {books_count} books.')
