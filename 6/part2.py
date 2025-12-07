#!/usr/bin/env -S uv run --script
#

import functools
import itertools
import operator
from sys import argv

# Define a reasonable type for the input, which will depend a lot on the problem


# Parse the input, stripping newlines and skipping blank lines
#
raw_map: dict[tuple[int, int], str] = {}
row = 0
with open(argv[1]) as infile:
    for line in infile.readlines():
        line = line.rstrip()  # don't strip left spaces
        if len(line) > 0:
            col = 0
            for c in line:
                raw_map[(col, row)] = c
                col += 1
        row += 1

# If needed, do some extra preprocessing, e.g. to create helper structures
#
width = max([_[0] for _ in raw_map.keys()])
height = max([_[1] for _ in raw_map.keys()])
breaks = []

for colnum in range(width):
    colchars = []
    for rownum in range(height):
        colchars.append(raw_map.get((colnum, rownum), " "))
    if all([_ == " " for _ in colchars]):
        breaks.append(colnum)
breaks.append(width + 1)  # so we can count the last set


# Define functions that operate oin the data to create answers
#
def op(sym: str):
    match sym:
        case "*":
            return operator.mul
        case "+":
            return operator.add
    raise Exception


# Basic testing
#


# Do the work
#

total = 0
last_break = -1
for b in breaks:
    op_symbol = raw_map[(last_break + 1, height)]
    values = []
    for c in range(b - 1, last_break, -1):
        values.append(int("".join([raw_map.get((c, r), "") for r in range(0, height)])))
        print(values, op_symbol)
    total += functools.reduce(op(op_symbol), values)
    last_break = b


# if argv[1] == "sample":
#     print(raw_map)

print(f"Part 2 answer: {total}")
