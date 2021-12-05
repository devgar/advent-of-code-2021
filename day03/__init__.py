#!/usr/bin/env python3

def most_frequent(l: []):
    return max(set(l), key = l.count)

def less_freaquent(l: []):
    return min(set(l), key = l.count)

def part1(input: str):
    report = input.splitlines()
    gamma = ''
    epsilon = ''
    for i in range(len(report[0])):
        bits = [report[j][i] for j in range(len(report))]

        frequent = most_frequent(bits)

        gamma += frequent
        epsilon += '0' if frequent == '1' else '1'
    print(int(gamma, 2) * int(epsilon, 2))

def part2(input: str):
    report = input.splitlines()
    oxygen = ''
    co2 = ''
    lines = range(len(report))
    for i in range(len(report[0])):
        ones = []
        zeros = []
        for j in lines:
            if report[j][i] == '0':
                zeros.append(j)
            else: ones.append(j)
        if len(ones) >= len(zeros):
            lines = ones
        else:
            lines = zeros
    oxygen = report[lines[0]]
    lines = range(len(report))
    for i in range(len(report[0])):
        ones = []
        zeros = []
        for j in lines:
            if report[j][i] == '0':
                zeros.append(j)
            else: ones.append(j)
        if len(ones) == 0 or len(zeros) <= len(ones) and len(zeros) > 0:
            lines = zeros
        else:
            lines = ones
    co2 = report[lines[0]]

    print(int(oxygen, 2) * int(co2, 2))



def main(input: str):
    part2(input)
