from collections import deque

import numpy as np


def dest_valid(area, visited, shape, src, dest):
    if (
        dest[0] < 0
        or dest[1] < 0
        or dest[0] >= shape[0]
        or dest[1] >= shape[1]
        or visited[dest]
        or area[dest] > area[src] + 1
    ):
        return False
    else:
        return True


def bfs(area: np.ndarray, startLoc: np.ndarray, endLoc: np.ndarray):
    visited = np.zeros_like(area)
    visited[startLoc] = 1
    shape = np.shape(area)

    d_row_col = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    q: deque[np.ndarray | tuple] = deque()
    q.append(startLoc)

    while q:
        src = q.popleft()
        for row, col in d_row_col:
            dest = (src[0] + row, src[1] + col)
            if dest_valid(area, visited, shape, src, dest):
                q.append(dest)
                visited[dest] = visited[src] + 1
                if dest == endLoc:
                    return int(visited[dest] - 1)


def main():
    with open("input.txt") as f:
        area = np.array([list(x.strip()) for x in f.readlines()])

    startLoc = np.where(area == "S")
    endLoc = np.where(area == "E")
    area[startLoc] = "a"
    area[endLoc] = "z"
    char_to_int = np.vectorize(lambda x: ord(x) - ord("a"))
    area = char_to_int(area)
    print(f"part one: {bfs(area, startLoc, endLoc)}")
    print(
        f"part two: {min([bfs(area, (row, 0), endLoc) for row in range(np.shape(area)[0])])}"
    )


if __name__ == "__main__":
    main()
