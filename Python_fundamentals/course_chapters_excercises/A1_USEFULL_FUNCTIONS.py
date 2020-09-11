def validate_key_existence(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dictionary(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


#SORTING BY 2 CRITERIA              el[0] - key     el[1] - value
#sorted_dict = dict(sorted(my_dict.items(), key=lambda el: (-el[1], el[0])))

