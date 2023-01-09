import re
from itertools import chain

import numpy as np


def calc_scenic_score(y, x, data) -> int:
    house = data[y, x]
    score = 1
    for direction in [
        data[y, x + 1 :],
        data[y, x - 1 :: -1],
        data[y + 1 :, x],
        data[y - 1 :: -1, x],
    ]:
        for view, tree in enumerate(direction, 1):
            if tree >= house:
                break
        score *= view
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        data = np.array(
            [list(map(int, re.findall(r"\d", line))) for line in f.readlines()]
        )
        size = data.shape[0]
        vis = np.zeros((size, size), dtype=np.int32)

        for _ in range(2):
            for y, row in enumerate(data):
                tallest = -1
                for x in chain(range(size), range(size - 2, -1, -1)):
                    if x == size - 1:
                        tallest = -1
                    if data[y, x] > tallest:
                        tallest = data[y, x]
                        vis[y, x] = 1
            data = data.T
            vis = vis.T
        print(f"part one: {vis.sum()}")

        for x in range(1, size - 1):
            for y in range(1, size - 1):
                vis[y, x] = calc_scenic_score(y, x, data)

        print(f"part two: {vis.max()}")
