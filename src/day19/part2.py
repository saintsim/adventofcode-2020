#!/usr/bin/env python3

import re

RULES = dict()


class Rule:
    def __init__(self, encoded_rule):
        self.encoded_rule = encoded_rule
        self.rule_decoded = False
        self.decoded_rule = ''

    def set_decoded_rule(self, decoded_rule):
        self.decoded_rule = decoded_rule
        all_done = True
        for i in decoded_rule:
            if str(i).isnumeric():
                all_done = False
        self.rule_decoded = all_done


def rule_checker(lines):
    messages = parse(lines)
    decode_rule(0)
    match = 0
    for message in messages:
        res = re.match(RULES[0].decoded_rule + '$', message)
        if res:
            match += 1
    return match


def decode_rule(i):
    if i == 8 or i == 11:
        print('hi')
    if RULES[i].rule_decoded:
        return RULES[i].decoded_rule
    decoded_elements = '('
    for element in RULES[i].encoded_rule.split():
        element = element.strip()
        if str(element).isnumeric():
            decoded_elements += decode_rule(int(element))
        else:
            if element[0] == '"':
                element = element[-2]
            decoded_elements += element
    decoded_elements += ')'
    if len(decoded_elements) == 3:
        decoded_elements = decoded_elements[-2]
    RULES[i].decoded_rule = decoded_elements
    return decoded_elements


def parse(lines):
    messages = []
    for line in lines:
        if line == '':
            continue
        if ':' in line:
            index, rule = line.split(':')
            RULES[int(index)] = Rule(rule.strip())
        else:
            messages.append(line)
    return messages


if __name__ == '__main__':
    with open('sample2', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(rule_checker(lines)))
