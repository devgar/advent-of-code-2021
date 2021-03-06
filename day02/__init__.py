#!/usr/bin/env python3

def __parseOrder(strOrder: str) -> [str, int]:
    order = strOrder.split(' ')
    order[1] = int(order[1])
    return order

def part1(input:str):
    orders = map(__parseOrder, input.splitlines())
    position = 0
    depth = 0

    for order in orders:
        # print(f"{order[0]} --> {order[1]}")
        if order[0] == 'forward':
            position += order[1]
        elif order[0] == 'up':
            depth -= order[1]
        else:
            depth += order[1]

    print(position * depth)

def part2(input: str):
    orders = map(__parseOrder, input.splitlines())
    position = 0
    aim = 0
    depth = 0

    for order in orders:
        if order[0] == 'up':
            aim -= order[1]
        elif order[0] == 'down':
            aim += order[1]
        else:
            position += order[1]
            depth += aim * order[1]
    print(position * depth)

def main(input: str):
    part2(input)
