import re

LINES = []


def setup_line(filename: str):
    LINES.clear()
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            LINES.append(line)


def setup_pattern(filename: str, pattern: str):
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(re.finditer(pattern, line))
    return lines


def part1(filename: str) -> int:
    reg_ex = r"\w+"
    sum = 0
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            words = re.finditer(reg_ex, line)
            for word in words:
                check_start = max(word.start() - 1, 0)
                check_end = min(word.end() + 1, len(LINES[i]) - 1)
                # Same line
                same_line = (word.start() > 0 and LINES[i][check_start] != ".") or (
                    word.end() < len(LINES[i]) - 1 and LINES[i][check_end - 1] != "."
                )
                # Previous line
                pre_line = (i >= 1) and any(
                    [
                        char != "." and not char.isnumeric()
                        for char in LINES[i - 1][check_start:check_end]
                    ]
                )
                # Next line
                next_line = (i <= (len(LINES) - 2)) and any(
                    [
                        char != "." and not char.isnumeric()
                        for char in LINES[i + 1][check_start:check_end]
                    ]
                )
                if same_line or pre_line or next_line:
                    sum += int(LINES[i][word.start() : word.end()])
    return sum


def part2(filename: str) -> int:
    sum = 0
    gears = setup_pattern(filename, r"\*")
    for i, gear_line in enumerate(gears):
        for gear in gear_line:
            number_lines = setup_pattern(filename, r"\w+")
            counter = 0
            prod = 1
            for number in number_lines[i]:
                if gear.start() in range(number.start() - 1, number.end() + 1):
                    counter += 1
                    prod *= int(LINES[i][number.start() : number.end()])
            if i > 0:
                for number in number_lines[i - 1]:
                    if gear.start() in range(number.start() - 1, number.end() + 1):
                        counter += 1
                        prod *= int(LINES[i - 1][number.start() : number.end()])
            if i < len(LINES) - 1:
                for number in number_lines[i + 1]:
                    if gear.start() in range(number.start() - 1, number.end() + 1):
                        counter += 1
                        prod *= int(LINES[i + 1][number.start() : number.end()])

            if counter == 2:
                sum += prod
    return sum


if __name__ == "__main__":
    setup_line("example")
    print(f"Part 1 example: {part1('example')}")
    print(f"Part 2 example: {part2('example')}")
    setup_line("input")
    print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 result: {part2('input')}")
