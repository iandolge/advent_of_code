from typing import Optional, Tuple


class Node:
    def __init__(
        self,
        name: str,
        parent: Optional["Node"] = None,
        size: int = 0,
        root: bool = True,
    ) -> None:
        self.size = size
        self.children: list[Node] = []
        self.name = name
        self.parent = parent
        self.root = root

    def cd(self, arg: str) -> "Node":
        if arg == "/" and not self.root:
            return self.parent.cd("/")  # type: ignore
        elif arg == "/" and self.root:
            return self
        elif arg == "..":
            return self.parent  # type: ignore
        else:
            return self.get_child(arg)

    def add_child(self, name: str, size=0) -> None:
        if name not in self.children:
            self.children.append(Node(name, self, size, root=False))

    def get_child(self, name: str) -> "Node":
        return self.children[[child.name for child in self.children].index(name)]

    def size_dir(self):
        MAX_SIZE = 100000
        size = self.size
        report_size = 0
        delete_size = {0}
        for child in self.children:
            c_size, c_rep_size, c_del_size = child.size_dir()
            size += c_size
            report_size += c_rep_size
            delete_size = delete_size | c_del_size

        if self.size == 0:
            delete_size = delete_size | {size}
            if size <= MAX_SIZE:
                report_size += size

        return [size, report_size, delete_size]

    def __contains__(self, name: str) -> bool:
        return name in [child.name for child in self.children]

    def __str__(self) -> str:
        return self.name


def solution(data: list[str]) -> Tuple[int, int]:
    MAX_STORAGE = 40_000_000
    cwd = Node("/")
    for line in data:
        match line.split():
            case ["$", "cd", arg]:
                cwd = cwd.cd(arg)
            case ["dir", name]:
                cwd.add_child(name)
            case ["$", "ls"]:
                pass
            case [size, name]:
                cwd.add_child(name, int(size))
    cwd = cwd.cd("/")

    tot_size, p1, dir_sizes = cwd.size_dir()
    p2 = min(dir for dir in dir_sizes if dir > tot_size - MAX_STORAGE)
    return (p1, p2)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
        print(f"solution: {solution(data)}")
