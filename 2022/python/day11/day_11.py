class Monkey:
    def __init__(self, details: str):
        self.num_inspections = 0
        for line in details.split("\n"):
            match line.strip().split(": "):
                case ["Starting items", items]:
                    self.items = list(map(int, items.split(", ")))
                case ["Operation", expr]:
                    match expr[10:].split():
                        case ["*", "old"]:
                            self.op = "^2"
                        case _:
                            self.op = expr[10:].split()[0]
                            self.scalar = int(expr[10:].split()[1])
                case ["Test", test]:
                    self.test = int(test[-2:])
                case ["If true", target]:
                    self.true_target = int(target[-1])
                case ["If false", target]:
                    self.false_target = int(target[-1])

    def __repr__(self):
        return str(self.num_inspections)

    def inspect(self, item):
        self.num_inspections += 1
        if self.op == "^2":
            return item**2
        elif self.op == "+":
            return item + self.scalar
        else:
            return item * self.scalar

    def add_items(self, items):
        self.items.extend(items)

    def consider_items(self):
        tests = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
        true_items = []
        false_items = []
        while self.items:
            self.items[0] = self.inspect(self.items[0])  # // 3 for part 1
            if self.items[0] % self.test == 0:
                true_items.append(self.items.pop(0) % tests)
            else:
                false_items.append(self.items.pop(0))
        return ((self.true_target, true_items), (self.false_target, false_items))

        # self.items.append(items)


def play_round(monkeys: list[Monkey]):
    for i in range(len(monkeys)):
        for target, items in monkeys[i].consider_items():
            monkeys[target].add_items(items)


def main():
    with open("input.txt") as f:
        lines = f.read()
    monkeys = []
    for monkey in lines.split("\n\n"):
        monkeys.append(Monkey(monkey))

    for i in range(10000):  # 20 for part 1
        play_round(monkeys)
    activity = [x.num_inspections for x in monkeys]
    activity.sort()
    monkey_business = activity[-1] * activity[-2]

    print(monkey_business)


if __name__ == "__main__":
    main()
