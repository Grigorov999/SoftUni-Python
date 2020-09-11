def data_types(data, n):
    result = ""

    if data == "int":
        result = int(n) * 2

    elif data == "real":
        result = f"{(float(n) * 1.5):.2f}"

    elif data == "string":
        result = "$" + n + "$"

    print(result)


data_type = input()
input_string = input()

data_types(data_type, input_string)
