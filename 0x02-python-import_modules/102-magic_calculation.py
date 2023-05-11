#!/usr/bin/python3

def magic_calculation(a, b):
    """Performs a magic calculation based on bytecode"""
    from magic_calculation_102 import add, sub
    # add, sub = __import__('magic_calculation_102', fromlist=('add', 'sub'))
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
