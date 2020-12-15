#!/usr/bin/env python3

from collections import Counter

SEEN_BEFORE = dict()
COUNT = Counter()


def number_spoken(lines):
    sequence = list(map(int, lines[0].split(',')))
    for idx, val in enumerate(sequence):
        add_item(idx, val)
    prev = sequence[-1]
    i = len(sequence)
    while i < 30000000:
        if COUNT[prev] < 2:
            next = 0
        else:
            next = SEEN_BEFORE[prev][1] - SEEN_BEFORE[prev][0]
        add_item(i, next)
        prev = next
        #print(i)
        i += 1
    return prev


def add_item(idx, val):
    if COUNT[val] > 0:
        SEEN_BEFORE[val] = [SEEN_BEFORE[val][-1], idx]
    else:
        SEEN_BEFORE[val] = [idx]
    COUNT[val] += 1


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(number_spoken(lines)))