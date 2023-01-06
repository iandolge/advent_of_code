def split_rounds(data):
    conv = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

    plays = [
        [conv[play] for play in line.split(" ")]
        for line in data.strip("\n").split("\n")
    ]
    return plays


def score_rounds(plays) -> int:
    result = {0: 3, 1: 6, -2: 6, 2: 0, -1: 0}
    return sum([me + result[me - them] for them, me in plays])


def part_one(data: str) -> int:
    plays = split_rounds(data)
    return score_rounds(plays)


def part_two(data: str) -> int:
    plays = split_rounds(data)
    plays = [[them, ((them + result) % 3) + 1] for them, result in plays]
    return score_rounds(plays)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
        print(f"{part_one(data) = }")
        print(f"{part_two(data) = }")
