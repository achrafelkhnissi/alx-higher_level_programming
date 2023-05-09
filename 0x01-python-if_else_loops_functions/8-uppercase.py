#!/usr/bin/python3

def uppercase(str):
    print("".join(map(lambda c: "{}".format(
        chr(ord(c) - 32)) if 'a' <= c <= 'z' else c, str)))
