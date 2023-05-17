#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        return sum([x * y for x, y in my_list]) / sum([y for x, y in my_list])
    return 0


if __name__ == '__main__':
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
    print("--")
    my_list = [(1, 2), (2, 1), (3, 0), (4, 0)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
    print("--")
    my_list = []
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
    print("--")
