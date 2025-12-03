#!/usr/bin/env -S uv run --script
#

from sys import argv
from typing import List, Tuple

input: List[List[int]] = []

with open(argv[1]) as infile:
    for line in infile.readlines():
        for r in line.split(','):
            try:
                start, end = r.split('-')
                input.append(list(range(int(start), int(end)+1)))
            except:
                pass


answer: int = 0

for l in input:
    for i in l:
        s = str(i)
        if len(s) % 2 != 0:
            continue
        m = len(s) // 2
        a, b = s[:m], s[m:]
        if a == b:
            print(s)
            answer += i

print(f"Answer: {answer}")
