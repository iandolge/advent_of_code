import re
from copy import deepcopy
from string import ascii_uppercase
from typing import Tuple


def split_input(data: str) -> Tuple[list[list[str]], list[list[int]]]:
    crates_input, inst_input = [part.splitlines() for part in data.split("\n\n")]
    n_stacks = len(re.findall(r"\d+", crates_input[-1]))

    crates_input.pop()
    crates_input.reverse()
    crates = []
    for i in range(1, n_stacks * 4, 4):
        crates.append([line[i] for line in crates_input if line[i] in ascii_uppercase])

    insts = [list(map(int, re.findall(r"\d+", line))) for line in inst_input]

    return (crates, insts)


def part_one(crates: list[list[str]], insts: list[list[int]]) -> str:
    for times, src, dest in insts:
        for _ in range(times):
            crates[dest - 1].append(crates[src - 1].pop())

    return "".join([stack[-1] for stack in crates])


def part_two(crates: list[list[str]], insts: list[list[int]]) -> str:
    for times, src, dest in insts:
        crates[dest - 1].extend(crates[src - 1][-times:])
        del crates[src - 1][-times:]

    return "".join([stack[-1] for stack in crates])


if __name__ == "__main__":
    with open("input.txt") as f:
        crates, insts = split_input(f.read())
        print(f"{part_one(deepcopy(crates), insts) = }")
        print(f"{part_two(deepcopy(crates), insts) = }")
