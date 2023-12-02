import re
import math
import typing as T

max_cube_possible = {"red": 12, "green": 13, "blue": 14}


def cube_number_list(line, color: str) -> T.List[str]:
    reg_ex = r"(\w+(?= " + color + r"))"
    return re.findall(reg_ex, line)


def is_color_possible(line, color) -> bool:
    res = cube_number_list(line, color)
    return len(res) == 0 or all([int(nb) <= max_cube_possible[color] for nb in res])


def min_nb_required(line, color) -> int:
    res = cube_number_list(line, color)
    return max([int(nb) for nb in res])


def part_1(filename: str) -> int:
    sum = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            game_id = re.findall(r"(\w+(?=:))", line)
            assert len(game_id) == 1
            if all([is_color_possible(line, color) for color in max_cube_possible]):
                sum += int(game_id[0])

    return sum


def part_2(filename: str) -> int:
    sum = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            sum += math.prod(
                [min_nb_required(line, color) for color in max_cube_possible]
            )

    return sum


if __name__ == "__main__":
    print(f"Part 1 example: {part_1('example')}")
    print(f"Part 1 result: {part_1('input')}")
    print(f"Part 2 result: {part_2('example')}")
    print(f"Part 2 result: {part_2('input')}")
