companies = {}

while True:

    company_info = input().split(" -> ")
    if company_info[0] == "End":
        break

    else:
        company = company_info[0]
        id = company_info[1]
        if company not in companies:
            companies[company] = []
        if id not in companies[company]:
            companies[company].append(id)

for employs in sorted(companies.items(), key=lambda x: x[0]):
    print(employs[0])
    [print(f"-- {x}") for x in employs[1]]
