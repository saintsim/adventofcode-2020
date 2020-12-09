#!/usr/bin/env python3


def previous_pairs(lines, preamble_amount):
    for x in range(preamble_amount, len(lines)):
        if not in_previous_set(lines[x], lines[x - preamble_amount:x]):
            return lines[x]


def in_previous_set(x, previous_set):
    for i in previous_set:
        if x-i in previous_set and i != x-i:
            return True
    return False


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [int(line.strip()) for line in file.readlines()]
        # for sample
        # print('Result: ' + str(previous_pairs(lines, 5)))
        print('Result: ' + str(previous_pairs(lines, 25)))
