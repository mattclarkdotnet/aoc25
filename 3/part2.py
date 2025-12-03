#!/usr/bin/env -S uv run --script
#


from sys import argv
from typing import List

# Define a reasonable type for the input, which will depend a lot on the problem
input: List[str] = []

# Parse the input, stripping newlines and skipping blank lines
with open(argv[1]) as infile:
    for line in infile.readlines():
        line = line.strip()
        if len(line) > 0:
            input.append(line)

# If needed, do some extra preprocessing, e.g. to create helper structures
pass


# Define functions that operate on the data to create answers


def best(number_str: str, maxdigits: int) -> str:
    bestvalue = 0
    bestdigit = ""
    digits = [
        int(char) for char in reversed(number_str)
    ]  # reversed so the index is also the decimal place, starting at zero
    for place, digit in enumerate(digits):
        value = digit * 10 ** min(place, maxdigits - 1)
        if value >= bestvalue:
            bestdigit = str(digit)
            bestvalue = value
    print(f"{number_str}: digit={bestdigit}")
    return bestdigit


def maxtwelve(cells: str) -> int:
    answer = ""
    for maxdigits in range(12, 0, -1):
        # find the highest valued available digit position
        bd = best(cells, maxdigits)
        answer += bd
        # eliminate all candidates "to the left of" the best we just found
        cells = cells[cells.find(bd) + 1 :]
    return int(answer)


# Execute primitive unit tests - essential for even the simpler problems
#
assert best("81171192", 4) == "8"
assert best("81171191", 1) == "9"

allpassed = True
for case, result in (
    ("987654321111111", 987654321111),
    ("811111111111119", 811111111119),
    ("818181911112111", 888911112111),
    ("234234234234278", 434234234278),
):
    m = maxtwelve(case)
    outcome = "OK" if m == result else "BAD"
    print(f"bank: {case}: expected {result}, got {m}: {outcome}")
    if m != result:
        allpassed = False
assert allpassed

# Generate the overall answer
answer: int = 0

for bank in input:
    m = maxtwelve(bank)
    print(f"{bank}: {m}")
    answer += m

print(f"Answer: {answer}")
