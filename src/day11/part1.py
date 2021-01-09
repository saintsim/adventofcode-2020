#!/usr/bin/env python3


def waiting_area(lines):
    seat_map = parse(lines)
    round = 0
    while True:
        print(round)
        new_seat_map = list(generate_new_seat_map(seat_map))
        if new_seat_map == seat_map:
            break
        seat_map = new_seat_map
        round += 1
    return occupied_count(seat_map)


def occupied_count(seat_map):
    return sum([row.count('#') for row in seat_map])


def generate_new_seat_map(seat_map):
    new_seat_map = []
    for x, line in enumerate(seat_map):
        new_row = []
        for y, cell in enumerate(line):
            new_row.append(new_value(x, y, seat_map))
        new_seat_map.append(new_row)
    return new_seat_map


def new_value(x, y, seat_map):
    # ABC  --> y
    # D.E  |
    # FGH  \/  x
    current = seat_map[x][y]
    if current == '.':
        return current
    adjacent_cells = [
        cell_value(x-1, y-1, seat_map),  # a
        cell_value(x-1, y, seat_map),    # b
        cell_value(x-1, y+1, seat_map),  # c
        cell_value(x, y-1, seat_map),    # d
        cell_value(x, y+1, seat_map),    # e
        cell_value(x+1, y-1, seat_map),  # f
        cell_value(x+1, y, seat_map),    # g
        cell_value(x+1, y+1, seat_map)   # h
    ]
    occupied_count = adjacent_cells.count('#')
    if current == 'L' and occupied_count == 0:
        return '#'
    if current == '#' and occupied_count >= 4:
        return 'L'
    return current


def cell_value(x, y, seat_map):
    if x < 0 or x >= len(seat_map):
        return '.'
    if y < 0 or y >= len(seat_map[0]):
        return '.'
    try:
        return seat_map[x][y]
    except:
        pass


def parse(lines):
    seat_map = []
    for line in lines:
        row = []
        for cell in line:
            row.append(cell)
        seat_map.append(row)
    return seat_map


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(waiting_area(lines)))