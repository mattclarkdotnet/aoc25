#!/usr/bin/env -S uv run --script
#

from sys import argv

# Define a reasonable type for the input, which will depend a lot on the problem

InputRanges = list[tuple[int, int]]
InputNumbers = list[int]
ranges: InputRanges = list(set())
numbers: InputNumbers = []

# Parse the input, stripping newlines and skipping blank lines
#
row = 0
with open(argv[1]) as infile:
    for line in infile.readlines():
        line = line.strip()
        if len(line) > 0:
            if "-" in line:
                (a, b) = [int(_) for _ in line.split("-")]
                ranges.append((a, b))
            else:
                numbers.append(int(line))

# If needed, do some extra preprocessing, e.g. to create helper structures
pass


# Define functions that operate oin the data to create answers
#


def fresh(ranges: InputRanges, number: int) -> bool:
    for r in ranges:
        if number >= r[0] and number <= r[1]:
            return True
    return False


# Basic testing
#

r = [(3, 6)]
assert fresh(r, 3)
assert not fresh(r, 7)


# Do the work
#

print(ranges, numbers)

answer: int = sum([1 if fresh(ranges, n) else 0 for n in numbers])
print(f"Answer part 1: {answer}")
