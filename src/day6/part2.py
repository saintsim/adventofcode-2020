#!/usr/bin/env python3


def size_of_intersection(lists):
    result = set(lists[0])
    for a_list in lists[1:]:
        result.intersection_update(a_list)
    return len(result)


def customs_form_sum(lines):
    total = 0
    group, groups = [], []
    for line in lines:
        if line == "\n":
            total += size_of_intersection(groups)
            groups = []
            continue
        for token in line:
            if token == "\n":
                continue
            group.append(token)
        groups.append(group)
        group = []
    total += size_of_intersection(groups)
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(customs_form_sum(lines)))
