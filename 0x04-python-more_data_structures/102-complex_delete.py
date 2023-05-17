#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        for key in list(a_dictionary.keys()):
            if a_dictionary[key] == value:
                del a_dictionary[key]
    return a_dictionary


if __name__ == '__main__':
    a_dictionary = {
        'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]
    }
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = complex_delete(a_dictionary, 'C')
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = complex_delete(a_dictionary, 'track')
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = complex_delete(a_dictionary, 'c')
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = complex_delete(a_dictionary, 89)
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = complex_delete(a_dictionary, [1, 2, 3])
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = complex_delete(a_dictionary, 'Number')
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")
