#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    last_digit_value = 0

    for roman_digit in numeral[::-1]:
        digit_value = roman_d[roman_digit]

        if digit_value >= last_digit_value:
            value += digit_value
            last_digit_value = digit_value
        else:
            value -= digit_value

    return value
