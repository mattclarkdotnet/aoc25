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


def not_contained_in(
    r: tuple[int, int], ranges: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    not_contained = []
    for range in ranges:
        if range[0] >= r[0] and range[1] <= r[1]:
            # range is contained within r
            not_contained.append(r)
    return not_contained


def contained_in(r: tuple[int, int], ranges: list[tuple[int, int]]) -> bool:
    for range in ranges:
        if range == []:
            return False
        if r[0] >= range[0] and r[1] <= range[1]:
            return True
    return False


def dedup(r: tuple[int, int], ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    deduped = []
    if contained_in(r, ranges):
        return ranges
    ranges = not_contained_in(r, ranges)

    # at this point we have an r and ranges which may overlap
    a, b = 0, 0
    for range in ranges:
        if range[0] <= r[0] <= range[1]:
            a = range[0] - 1
        if range[0] <= r[1] <= range[1]:
            b = range[1] + 1
        if b >= a:
            deduped.append((a, b))
    deduped.append(ranges)
    return deduped


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

deduped = []
for r in ranges:
    print(r, deduped)
    deduped.append(dedup(r, deduped))
count = sum((b - a) + 1 for a, b in deduped)
if argv[1] == "sample":
    print(deduped, count)

print(f"Answer part 2: {count}")
