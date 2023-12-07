import re
from math import sqrt


# Solve ax^2+bx+c=0
def _solve_function(a: int, b: int, c: int) -> (int, int):
    delta = b**2-4*a*c
    return ((-b - sqrt(delta))/(2*a), (-b + sqrt(delta))/(2*a))


def _get_times_and_distance(filename: str):
    regex = r"[\d]\w+|\d"
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if len(re.findall("Time: ", line)) > 0:
                times = re.findall(regex, line)
                continue
            if len(re.findall("Distance: ", line)) > 0:
                distances = re.findall(regex, line)
    return times, distances


def part1(filename: str) -> int:
    ret = 1

    times, distances = _get_times_and_distance(filename)
    for time, distance in zip(times, distances):
        start, end = _solve_function(1, -int(time), int(distance))
        if start >= int(start):
            start = int(start) + 1
        if end == int(end):
            end = int(end) - 1
        ret *= int(end) - int(start) + 1

    return ret


def part2(filename: str) -> int:
    ret = 1

    times, distances = _get_times_and_distance(filename)
    real_time = ""
    real_distance = ""
    for time, distance in zip(times, distances):
        real_time += time
        real_distance += distance

    start, end = _solve_function(1, -int(real_time), int(real_distance))
    if start >= int(start):
        start = int(start) + 1
    if end == int(end):
        end = int(end) - 1
    return int(end) - int(start) + 1


if __name__ == "__main__":
    print(f"Part 1 example: {part1('example')}")
    print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 example: {part2('example')}")
    print(f"Part 2 result: {part2('input')}")
