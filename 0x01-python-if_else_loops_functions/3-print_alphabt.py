#!/usr/bin/python3
for lowercase_letters in range(97, 123):
    if chr(lowercase_letters) != 'q' and chr(lowercase_letters) != 'e':
    print("{}".format(chr(lowercase_letters)), end="")
