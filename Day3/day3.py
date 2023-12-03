import typing as T
import re

LINES = []


def setup_line(filename: str):
    LINES.clear()
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            LINES.append(line)


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
                # print(LINES[i][word.start():word.end()])
                # print(same_line)
                if same_line:
                    print(LINES[i][check_start])
                    print(LINES[i][check_end])
                # print(pre_line)
                # print(next_line)
                if same_line or pre_line or next_line:
                    print(f"Nb to add: {LINES[i][word.start():word.end()]}")
                    sum += int(LINES[i][word.start() : word.end()])
    return sum


if __name__ == "__main__":
    setup_line("example")
    print(f"Part 1 example: {part1('example')}")
    setup_line("input")
    print(f"Part 1 result: {part1('input')}")
