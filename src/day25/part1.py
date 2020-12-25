#!/usr/bin/env python3


def encryption_key(file):
    key1, key2 = parse(file)
    # loop_size1 = decrypt(7, key1, None)
    loop_size2 = decrypt(7, key2, None)
    return decrypt(key1, None, loop_size2)


def decrypt(subject_number, target, target_loop_size):
    current_value = 1
    loop_size = 0
    while True:
        if target_loop_size:
            if loop_size == target_loop_size:
                return current_value
        elif current_value == target:
            return loop_size
        current_value *= subject_number
        current_value = current_value - (20201227 * (current_value // 20201227))
        loop_size += 1


def parse(file):
    return list(map(int, file.split('\n')))


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(encryption_key(file.read())))