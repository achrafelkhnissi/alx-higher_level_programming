#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


if __name__ == '__main__':
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")
