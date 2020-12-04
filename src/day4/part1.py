#!/usr/bin/env python3

def passport_check(lines):
    passports = parse_passport_data(lines)
    valid_passports = 0
    for passport in passports:
        if len(passport) == 7:
            valid_passports += 1
    return valid_passports


def parse_passport_data(lines):
    passports = []
    passport = dict()
    for line in lines:
        if line == "\n":
            passports.append(passport)
            passport = dict()
            continue
        for token in line.split(" "):
            token = token.strip()
            key_value = token.split(":")
            if key_value[0] != "cid":
                passport[key_value[0]] = key_value[1]
    passports.append(passport)
    return passports


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(passport_check(lines)))