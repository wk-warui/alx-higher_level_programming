#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers == 99:
        print(f"{numbers:d}")
    else:
        print(f"{numbers:02}, end=", ")
