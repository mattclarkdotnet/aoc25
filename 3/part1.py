#!/usr/bin/env -S uv run --script
#

from sys import argv
from typing import List

# Define a reasonable type for the input, which will depend a lot on the problem
input: List[List[int]] = []

# Parse the input, stripping newlines and skipping blank lines
with open(argv[1]) as infile:
    for line in infile.readlines():
        line = line.strip()
        if len(line) > 0:
            input.append([int(v) for v in line])

# If needed, do some extra preprocessing, e.g. to create helper structures
pass


# Define functions that operate oin the data to create answers
def maxtwo(cells: List[int]) -> int:
    highest = max(
        cells[:-1]
    )  # the highest number in the last position in the bank is never useful because it is in the "ones place" in the answer
    ihighest = cells.index(highest)
    nexthighest = max(cells[ihighest + 1 :])
    return int(str(f"{highest}{nexthighest}"))


# Execute primitive unit tests - essential for even the simpler problems
allpassed = True
for case, result in (
    ([1, 9, 7, 3, 4], 97),
    ([1, 9, 7, 3, 4], 97),
    ([1, 7, 4, 3, 9], 79),
):
    m = maxtwo(case)
    print(f"bank: {case}: expected {result}, got {m}")
    if m != result:
        allpassed = False
assert allpassed

# Generate the overall answer
answer: int = 0

for bank in input:
    m = maxtwo(bank)
    print(f"{bank}: {m}")
    answer += m

print(f"Answer: {answer}")
