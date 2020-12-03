#!/usr/bin/env python3

MAZE = []


def maze_trees(lines):
    init_maze(lines)
    return traverse_maze()


def traverse_maze():
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
        x += 3
        y += 1


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