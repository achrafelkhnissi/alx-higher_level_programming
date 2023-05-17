#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


if __name__ == '__main__':
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level"}
    new_dict = simple_delete(a_dictionary, 'track')
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = simple_delete(a_dictionary)
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")
