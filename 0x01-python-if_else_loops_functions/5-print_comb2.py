#!/usr/bin/python3

for i in range(0, 100):
    print(f"{i:02d}", end="")
    print(", ", end="") if i < 99 else print("")
