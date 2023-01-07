def item_priority(item: int) -> int:
    return item + (27 - ord("A") if item < ord("a") else 1 - ord("a"))


def part_one(data: list[str]) -> int:
    priority = 0
    for line in data:
        left = set(line[: len(line) // 2])
        right = set(line[len(line) // 2 :])
        common = ord(list(left.intersection(right))[0])
        priority += item_priority(common)

    return priority


def part_two(data: list[str]) -> int:
    priority = 0
    for i in range(0, len(data), 3):
        badge = ord(
            list(set(data[i]).intersection(set(data[i + 1]), set(data[i + 2])))[0]
        )
        priority += item_priority(badge)

    return priority


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
        print(f"{part_one(data) = }")
        print(f"{part_two(data) = }")
