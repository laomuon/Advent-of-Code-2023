import re
import math


def part1(filename: str) -> int:
    ret = 0
    pattern = None
    pattern_len = 0
    map_dict = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words = re.findall(r"\w+", line)
            if len(words) == 1:
                pattern = words[0]
                pattern_len = len(pattern)
            elif len(words) == 3:
                map_dict[words[0]] = {"L": words[1], "R": words[2]}

    starting_point = "AAA"
    while (starting_point != "ZZZ"):
        starting_point = map_dict[starting_point][pattern[ret % pattern_len]]
        ret += 1
    return ret


def part2(filename: str) -> int:
    ret = 0
    pattern = None
    pattern_len = 0
    map_dict = {}
    starting_points = {}
    ending_points = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words = re.findall(r"\w+", line)
            if len(words) == 1:
                pattern = words[0]
                pattern_len = len(pattern)
            elif len(words) == 3:
                map_dict[words[0]] = {"L": words[1], "R": words[2]}
                if words[0][-1] == "A":
                    starting_points[words[0]] = None
                if words[0][-1] == "Z":
                    ending_points[words[0]] = None

    # for pt in ending_points:
    #     start_pt = pt
    #     count = 0
    #     while (True):
    #         start_pt = map_dict[start_pt][pattern[count % pattern_len]]
    #         count += 1
    #         if start_pt == pt:
    #             ending_points[pt] = count
    #             break
    #
    for pt in starting_points:
        start_pt = pt
        count = 0
        while (True):
            start_pt = map_dict[start_pt][pattern[count % pattern_len]]
            count += 1
            if start_pt[-1] == 'Z':
                starting_points[pt] = [start_pt, count]
                break

    return math.lcm(*[r[1] for r in starting_points.values()])
    # while (True):
    #     for r, s in zip(rets, starting_points):
    #         r += ending_points[starting_points[s][0]]
    #     if all([r == rets[0] for r in rets]):
    #         return rets[0]
    # return ret


if __name__ == "__main__":
    # print(f"Part 1 example: {part1('example2')}")
    # print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 example: {part2('example3')}")
    print(f"Part 2 result: {part2('input')}")
