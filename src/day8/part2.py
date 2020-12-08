#!/usr/bin/env python3

from src.day8.part1 import parse
from copy import deepcopy


def accumulator(lines):
    program = parse(lines)
    for line_to_change in range(len(program)):
        new_program = change_line_x(deepcopy(program), line_to_change)
        if new_program:
            run_output = run_program(new_program)
            if run_output:
                return run_output


def change_line_x(program, line_to_change):
    instruction = program[line_to_change]
    if instruction.operation in ['nop', 'jmp']:
        program[line_to_change].operation = 'nop' if instruction.operation == 'jmp' else 'jmp'
    else:
        return None
    return program


def run_program(program):
    total, i, lines_visited = 0, 0, set()
    while i < len(program):
        if i in lines_visited:
            return None
        else:
            lines_visited.add(i)
        op, val = program[i].operation, program[i].value
        if op == 'acc':
            total += val
        elif op == 'jmp':
            i = i + val
            continue
        i += 1
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(accumulator(lines)))
