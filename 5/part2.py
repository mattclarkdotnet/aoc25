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
pass


# Do the work
#

sorted_ranges = sorted(ranges, key=lambda _: _[0])
if argv[1] == "sample":
    print(sorted_ranges)


total = 0
merged_ranges = []
key = 0
largest = max([_[1] for _ in ranges])

while key <= largest:
    # get the lowest start number
    start = min([_[0] for _ in ranges if _[0] >= key])
    print(f"start: {start}")
    # find the largest range with that start number
    end = max([_[1] for _ in ranges if _[0] == start])
    print(f"end: {end}")

    while True:
        # find all the ranges that start within or immeditaely after (start, end)
        # and end after (start, end)
        overlapping = [_ for _ in ranges if start < _[0] <= end + 1 and _[1] > end]
        if len(overlapping) > 0:
            # extend 'end' to the largest overlapping end
            print(f"overlapping: {overlapping}")
            new_end = max([_[1] for _ in overlapping])
            print(f"extending end from {end} to {new_end}")
            end = new_end
        else:
            print(f"made range ({start},{end})")
            total += end - start + 1
            merged_ranges.append((start, end))
            break
    key = (
        end + 2
    )  # all ranges with smaller starts than this must have been included by now


if argv[1] == "sample":
    print(merged_ranges)

print(f"Answer part 2: {total}")
