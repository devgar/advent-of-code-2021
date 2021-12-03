

def parseNumbers(input: str) -> [str]:
    return [int(num) for num in input.strip().split("\n")]


def part1(input: str):

    numbers = parseNumbers(input)

    last = None
    increased = 0
    decreased = 0


    for num in numbers:
        if last != None:
            if num > last: increased += 1
            elif num < last: decreased += 1
            else: print(f"Equals! {num} = {last}")
    
        last = num

    print(f"(Increased: {increased}")
    print(f"(Decreased: {decreased}")


def part2(input: str):

    numbers = parseNumbers(input)
    groups = [numbers[i] + numbers[i+1] + numbers[i+2] for i in range(len(numbers) -2)]

    last = groups[0]
    increased = 0
    decreased = 0
    equals = 0

    for group in  groups[1:]:
        if last < group: increased += 1
        elif last > group: decreased += 1
        else: equals += 1
        last = group
    print(increased)
    print(decreased)
    print(equals)
def main(input: str):
    part2(input)

if __name__ == "__main__":
    from sys import argv
    main(" ".join(argv[1:]))
