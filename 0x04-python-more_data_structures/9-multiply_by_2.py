#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}


if __name__ == '__main__':
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = multiply_by_2(a_dictionary)
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")

    new_dict = multiply_by_2(a_dictionary)
    print(sorted(list(new_dict.items())))
    print("--")
    print(sorted(list(a_dictionary.items())))
    print("--")
