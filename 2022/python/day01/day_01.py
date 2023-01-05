def elf_food(data: str) -> list[int]:
    elves = [
        sum(map(int, each_elf.split("\n"))) for each_elf in data.strip().split("\n\n")
    ]
    return elves


def part_one(data: str) -> int:
    return max(elf_food(data))


def part_two(data: str) -> int:
    elves = elf_food(data)
    return sum(sorted(elves)[-3:])


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
        print(f"{part_one(data) = }")

        print(f"{part_two(data) = }")
