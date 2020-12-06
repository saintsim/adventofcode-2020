#!/usr/bin/env python3


def size_of_intersection(lists):
    intersection_set = set(lists[0])
    for this_list in lists[1:]:
        intersection_set.intersection_update(this_list)
    return len(intersection_set)


def customs_form_sum(lines):
    total, groups = 0, []
    for line in lines:
        group = set()
        if line == "\n":
            total += size_of_intersection(groups)
            groups = []
        else:
            [group.add(token) for token in line if token != '\n']
            groups.append(group)
    return total + size_of_intersection(groups)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(customs_form_sum(file.readlines())))
