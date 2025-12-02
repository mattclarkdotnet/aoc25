#!/usr/bin/env -S uv run --script
#

from sys import argv
from typing import List, Tuple

input: List[Tuple[str, int]] = []

with open(argv[1]) as infile:
    for line in infile.readlines():
        input.append((line[0], int(line[1:])))


def sign(n: int) -> int:
    if n == 0:
        return 0
    return -1 if n < 0 else 1


def zeroes(p: int, r: int) -> int:
    assert r != 0
    p_new = p + r
    z = 1 if p_new % 100 == 0 else 0  # count the case where we land on zero exactly
    # however we also need to account for crossing zero, remembering that we always start with a positive number or zero
    z += abs(p_new // 100)
    if p_new < 0 and p == 0:
        # deal with examples where the result is negative despite not crossing zero
        # for example p == 0, r == -15.  abs(-15//100) is 1
        z -= 1
    elif p_new > 99 and p_new % 100 == 0:
        # deal with examples where we'd be double counting
        z -= 1
    return z


testcases = [
    (99, 1, 1),
    (1, -1, 1),
    (0, 1, 0),
    (0, -1, 0),
    (0, 2, 0),
    (0, -2, 0),
    (0, 100, 1),
    (0, -100, 1),
    (0, 150, 1),
    (0, -150, 1),
    (0, 200, 2),
    (0, -200, 2),
    (0, 250, 2),
    (0, -250, 2),
    (50, 155, 2),
    (10, -55, 1),
    (10, 155, 1),
    (10, -155, 2),
    (32, -30, 0),
    (70, 48, 1),
]
for p, r, o in testcases:
    result = zeroes(p, r)
    print(f"Testing {p} + {r} = {p + r} : expected {o} got {result}")
    assert result == o

pos: int = 50
pw: int = 0

for direction, rotation in input:
    lastpw = pw
    if direction == "L":
        rotation = -rotation
    pw = pw + zeroes(pos, rotation)
    print(f"{pos} + {rotation} = {pos + rotation} : zeroes = {pw - lastpw}")
    pos = (pos + rotation) % 100

print(f"Solution: {pw}")
assert pw == 5933
