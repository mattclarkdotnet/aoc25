#!/usr/bin/env -S uv run --script
#

import functools
import itertools
import operator
from sys import argv

# Define a reasonable type for the input, which will depend a lot on the problem


# Parse the input, stripping newlines and skipping blank lines
#
rows: list[list[int]] = []
symbols = []
with open(argv[1]) as infile:
    for line in infile.readlines():
        line = line.strip()
        if len(line) > 0:
            try:
                rows.append([int(_) for _ in line.split() if _ != ""])
            except Exception:
                symbols = [_ for _ in line.split() if _ != ""]


# If needed, do some extra preprocessing, e.g. to create helper structures
pass


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

operators = [op(_) for _ in symbols]
total = 0
for col in range(len(rows[0])):
    vals = [_[col] for _ in rows]
    result = functools.reduce(operators[col], vals)
    print(f"{symbols[col].join([' ' + str(_) + ' ' for _ in vals])} = {result}")
    total += result

if argv[1] == "sample":
    print(rows, symbols)

print(f"Part 1 answer: {total}")
