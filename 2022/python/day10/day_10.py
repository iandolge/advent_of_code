if __name__ == "__main__":
    with open("input.txt") as f:
        commands = [
            int(line.split()[1]) if len(line.split()) == 2 else None
            for line in f.readlines()
        ]
    p1_key_cycles = [20, 60, 100, 140, 180, 220]
    x = 1
    p1_cycle = 1
    p1_sum = 0

    p2_pixels = ""
    p2_scan = 0

    def draw_pixel(x, scan):
        return "#" if abs(x - scan) <= 1 else "."

    for cmd in commands:
        p1_cycle += 1

        p2_pixels += draw_pixel(x, p2_scan)
        p2_scan = (p2_scan + 1) % 40
        if cmd:
            p1_cycle += 1

            p2_pixels += draw_pixel(x, p2_scan)
            p2_scan = (p2_scan + 1) % 40
            x += cmd

        if list(filter(lambda x: p1_cycle in range(x - 1, x + 1), p1_key_cycles)):
            p1_sum += x * p1_key_cycles.pop(0)

    print(f"part one: {p1_sum}")

    width = 40
    screen = "\n".join(
        [p2_pixels[i : i + width] for i in range(0, len(p2_pixels), width)]
    )
    print(f"part two: \n{screen}")
