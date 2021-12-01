#!/usr/bin/env  python3

from sys import argv, stderr

import requests

if len(argv) < 2:
    print("An argument (day) is needed", file=stderr)
    exit(1)
day = int(argv[1])

session=""

with open(".session") as file:
    session = file.read().splitlines()[0]

cookies = dict(session=session)

r = requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=cookies)

print(r.text)

