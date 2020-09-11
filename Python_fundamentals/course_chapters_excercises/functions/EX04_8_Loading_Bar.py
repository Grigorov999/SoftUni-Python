def loading_bar(n):
    if 0 <= n < 100:
        str_percent = "%" * int(n / 10)
        str_dot = "." * int(10 - n / 10)
        print(f"{n}% [{str_percent + str_dot}]")
        print("Still loading...")

    elif n == 100:
        str_percent = "%" * int(n / 10)
        print(f"{n}% Complete!")
        print(f"[{str_percent}]")


loading = int(input())
loading_bar(loading)
