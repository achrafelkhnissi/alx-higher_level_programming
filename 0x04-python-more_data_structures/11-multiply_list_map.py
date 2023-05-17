#!/usr/bin/python3

def mutiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    new_list = mutiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)
