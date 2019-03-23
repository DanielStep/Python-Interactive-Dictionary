import json
from difflib import get_close_matches

"""
Globals
"""
data = {}

"""
Functions
"""


def load_data():
    return json.load(open("data.json", 'r'))


def user_input():
    return input("Enter word for definition: ").lower()


def get_dict_value(key):
    if key in data:
        return data[key]

    elif len(get_closest_match(key)) > 0:
        return choose_match(key)

    return []


def choose_match(key):
    match = get_closest_match(key)[0]
    yn = input("Did you mean %s instead? (y/n) " % match)
    if yn is "y":
        return data[match]
    elif yn is "n":
        return []
    else:
        return "Invalid input."


def get_closest_match(key):
    return get_close_matches(key, data.keys())


def print_result(values):
    if type(values) is str:
        print(values)

    elif type(values) is list:
        if values:
            print_values(values)
        else:
            print("No definitions were found.")


def print_values(values):
    for value in values:
        position = str(values.index(value) + 1) + ". "
        print(position + value)


"""
Run App
"""
operate = True

data = load_data()

while operate is True:
    result = get_dict_value(user_input())
    print_result(result)
