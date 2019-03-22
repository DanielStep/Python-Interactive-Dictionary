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
    return input("Enter word for definition: ")


def get_dict_value(key):
    match = get_closest_match(key)
    if match in data:
        return data[match]
    else:
        return []


def get_closest_match(key):
    keys = data.keys()
    key = key.lower()
    return get_close_matches(key, keys)[0]


def print_values(values):
    if values:
        for value in values:
            print(value)
    else:
        print("No definitions were found.")


"""
Run Dictionary
"""
data = load_data()
result = get_dict_value(user_input())
print_values(result)
