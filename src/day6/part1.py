#!/usr/bin/env python3


def customs_form_sum(lines):
    total = 0
    group = set()
    for line in lines:
        if line == "\n":
            total += len(group)
            group = set()
            continue
        for token in line:
            if token == "\n":
                continue
            group.add(token)
    total += len(group)
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(customs_form_sum(lines)))
