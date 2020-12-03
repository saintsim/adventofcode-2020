#!/usr/bin/env python3

MAZE = []


def maze_trees(lines):
    init_maze(lines)
    return traverse_maze(1, 1) * traverse_maze(3, 1) * traverse_maze(5, 1) * traverse_maze(7, 1) * traverse_maze(1,2)


def traverse_maze(x_change, y_change):
    #  x --->
    #        !
    #        \/
    #         y
    x = 0
    y = 0
    tree_count = 0
    while True:
        if y >= len(MAZE):
            return tree_count
        cell_contents = MAZE[y][x % len(MAZE[0])]
        if cell_contents is "#":
            tree_count += 1
        x += x_change
        y += y_change


def init_maze(lines):
    for line in lines:
        row = []
        for cell in line:
            row.append(cell)
        MAZE.append(row)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(maze_trees(lines)))