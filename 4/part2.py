#!/usr/bin/env -S uv run --script
#

import itertools
from sys import argv
from typing import Dict, Iterable, Tuple

# Define a reasonable type for the input, which will depend a lot on the problem

Position = tuple[int, int]
InputMap = Dict[Position, bool]
input: InputMap = {}

# Parse the input, stripping newlines and skipping blank lines
#
row = 0
width = 0
with open(argv[1]) as infile:
    for line in infile.readlines():
        line = line.strip()
        if len(line) > 0:
            width = max(len(line), width)
            for col, char in enumerate(line):
                input[(col, row)] = True if char == "@" else False
            row += 1
height = row

print(f"w:{width}, h:{height}")

# If needed, do some extra preprocessing, e.g. to create helper structures
pass


# Define functions that operate oin the data to create answers
#
adjacencies = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
adjacencies.remove((0, 0))
assert len(adjacencies) == 8


def neighbouring(input: InputMap, position: Position) -> Iterable[Position]:
    for x, y in adjacencies:
        yield Position((position[0] + x, position[1] + y))


def neighbour_vals(input: InputMap, position: Position) -> Iterable[bool]:
    for n in neighbouring(input, position):
        yield input.get(n, False)


def accessible(input: InputMap) -> Iterable[Position]:
    for x in range(width):
        for y in range(height):
            if input[(x, y)] is True:
                rolls = sum(1 for i in neighbour_vals(input, (x, y)) if i is True)
                if rolls < 4:
                    yield (x, y)


if argv[1] == "input":
    assert input[(0, 2)] is True
    assert input[(1, 1)] is True
    assert input[(1, 2)] is True
    assert input[(2, 3)] is True
    assert input[(0, 0)] is False
    assert input[(0, 1)] is False
    assert input[(2, 0)] is False
    assert input[(3, 4)] is False
    assert input[(0, 3)] is False

removed = 0
while True:
    rolls = list(accessible(input))
    if len(rolls) > 0:
        removed += len(rolls)
        print(f"Removed {len(rolls)}")
        for r in rolls:
            input[r] = False
    else:
        print(f"Answer: {removed}")
        break
