DIR_MAP = {
    "U": complex(0, 1),
    "D": complex(0, -1),
    "R": complex(1, 0),
    "L": complex(-1, 0),
}
ROPEMAX = 1.5  # greater than sqrt(2)


def move_rope_tail(rope: complex) -> complex:
    return complex(min(max(rope.real, -1), 1), min(max(rope.imag, -1), 1))


if __name__ == "__main__":
    with open("input.txt") as f:
        directions = "".join(
            [row.split()[0] * int(row.split()[1]) for row in f.readlines()]
        )

        rope = [complex(0, 0)] * 10
        p1_tail_locs = {complex(0, 0)}
        p2_tail_locs = {complex(0, 0)}
        for move in directions:
            rope[0] += DIR_MAP[move]
            for i in range(1, len(rope)):
                if abs(length := rope[i - 1] - rope[i]) > ROPEMAX:
                    rope[i] += move_rope_tail(length)
            p1_tail_locs.add(rope[1])
            p2_tail_locs.add(rope[9])

        print(f"part one: {len(p1_tail_locs)}")
        print(f"part two: {len(p2_tail_locs)}")
