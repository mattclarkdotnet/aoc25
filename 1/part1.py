#!/usr/bin/env -S uv run --script
#

from sys import argv
from typing import List, Tuple

input: List[Tuple[str, int]] = []

with open(argv[1]) as infile:
    for line in infile.readlines():
        input.append((line[0], int(line[1:])))

print(input, "\n")

pos = 50
pw = 0

for d, v in input:
    if d == "L":
        v = -v
    pos = (pos + v) % 100
    if pos == 0:
        pw += 1

print(f"Solution: {pw}")
