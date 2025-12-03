#!/usr/bin/env -S uv run --script
#

from sys import argv
from typing import List, Tuple

input: List[int] = []

with open(argv[1]) as infile:
    for line in infile.readlines():
        for r in line.split(','):
            try:
                start, end = r.split('-')
                input.extend([_ for _ in range(int(start), int(end)+1)])
            except:
                pass



def check(i: int) -> bool:
    s = str(i)
    for stride in range(1, len(s) // 2 + 1):
        substrs = [s[a:a+stride] for a in range(0, len(s), stride)]
        if len(set(substrs)) == 1:
            return True
    return False

assert check(11)
assert check(1212)
assert check(333)

answer: int = 0

for i in input:
    if check(i):
        print(i)
        answer += i


print(f"Answer: {answer}")
