from collections import deque


def parse_data(data: str, n_chars) -> int:
    scanner = deque(data[:n_chars], n_chars)
    for i in range(4, len(data)):
        if len(set(scanner)) == n_chars:
            break
        scanner.append(data[i])
    return i


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
        print(f"part one: {parse_data(data, 4)}")
        print(f"part two: {parse_data(data, 14)}")
