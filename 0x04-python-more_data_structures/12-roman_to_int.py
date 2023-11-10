#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        if i > 0 and r_dic[roman_string[i]] > r_dic[roman_string[i - 1]]:
            total += r_dic[roman_string[i]] - 2 * r_dic[roman_string[i - 1]]
        else:
            total += r_dic[roman_string[i]]

    return total
