import re


def split_input(data: str) -> list[list[int]]:
    return [list(map(int, re.findall(r"\d+", line))) for line in data.splitlines()]


def elf_assignments(line: list[int]) -> tuple[set, set]:
    elf_1 = set(range(line[0], line[1] + 1))
    elf_2 = set(range(line[2], line[3] + 1))
    return elf_1, elf_2


def part_one(data: list[list[int]]) -> int:
    result = 0
    for line in data:
        elf_1, elf_2 = elf_assignments(line)
        if elf_1 & elf_2 in (elf_1, elf_2):
            result += 1
    return result


def part_two(data: list[list[int]]) -> int:
    result = 0
    for line in data:
        elf_1, elf_2 = elf_assignments(line)
        if len(elf_1 | elf_2) < len(elf_1) + len(elf_2):
            result += 1
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = split_input(f.read())
        print(f"{part_one(data) = }")
        print(f"{part_two(data) = }")
