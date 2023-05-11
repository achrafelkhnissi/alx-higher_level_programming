#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    sum = 0
    for i in range(1, length):
        sum += int(argv[i])
    print("{}".format(sum))
