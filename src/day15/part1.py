#!/usr/bin/env python3


def number_spoken(lines):
    sequence = list(map(int, lines[0].split(',')))
    i = len(sequence)
    prev = sequence[-1]
    while i < 2020:
        if prev not in sequence[:-1]:
            next = 0
        else:
            past_occurences = [i for i, x in enumerate(sequence) if x == prev]
            next = past_occurences[-1] - past_occurences[-2]
        sequence.append(next)
        prev = next
        i += 1
    return prev


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(number_spoken(lines)))