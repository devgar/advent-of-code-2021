


def main(input: str):

    numbers = [int(num) for num in input.strip().split("\n")]

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




if __name__ == "__main__":
    from sys import argv
    main(" ".join(argv[1:]))
