#!/usr/bin/env python3

import re


def password_checker(lines):
    valid_password_count = 0
    for line in lines:
        if password_is_valid(line):
            valid_password_count = valid_password_count+1
    return valid_password_count


def password_is_valid(line):
    min_amount, max_amount, char_to_check, password = re.search('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line).groups()
    char_count = 0
    for element in password:
        if element is char_to_check:
            char_count = char_count + 1
    return int(min_amount) <= char_count <= int(max_amount)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(password_checker(lines)))