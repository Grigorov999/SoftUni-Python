def password_check(n):
    length = False
    chr_num = False
    two_nums_min = False

    if not 6 <= len(n) <= 10:
        print("Password must be between 6 and 10 characters")
    else:
        length = True

    if not n.isalnum():
        print("Password must consist only of letters and digits")
    else:
        chr_num = True

    if sum(i.isdigit() for i in n) < 2:
        print("Password must have at least 2 digits")
    else:
        two_nums_min = True

    if length and chr_num and two_nums_min:
        print("Password is valid")


password = input()

password_check(password)
