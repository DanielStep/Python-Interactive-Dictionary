import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = {}

def load_data():
    return json.load(open("data.json", 'r'))

def user_input():
    return input("Enter word for definition: ")

def get_dict_value(key):
    key = key.lower()
    match = get_closest_match(key)
    if match in data:
        return data[match]
    else:
        return []

def get_closest_match(key):
    keys = data.keys()
    return get_close_matches(key, keys)[0]

def print_values(values):
    if values:
        for value in values:
            print(value)
    else:
        print("No definitions were found.")

data = load_data()
values = get_dict_value( user_input() ) 
print_values(values)