import re
import typing as T
import math


def _calculate_diffs(input_list: T.List[int], level: int, index: int):
    ret = 0
    for i in range(len(input_list)-1):
        ret += input_list[index+level-i] * math.comb(level, i) * (-1)**i
    return ret


def _calculate_diffs_list(input_list: T.List[int], level: int):
    ret = []
    for i in range(len(input_list) - level):
        ret.append(_calculate_diffs(input_list, level, i))
    if all([r == 0 for r in ret]):
        return None
    return ret


def part1(filename: str) -> int:
    ret = 0
    res = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            nbs = [int(nb) for nb in re.findall(r"[\-a-zA-Z0-9_]+", line)]
            if len(nbs) == 0:
                break
            for i in range(len(nbs)):
                res_list = _calculate_diffs_list(nbs, i)
                if res_list is None:
                    break
                res.append(res_list)
        for i in res:
            ret += i[-1]
    return ret


def part2(filename: str) -> int:
    ret = 0
    res = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            nbs = [int(nb) for nb in re.findall(r"[\-a-zA-Z0-9_]+", line)]
            nbs.reverse()
            if len(nbs) == 0:
                break
            for i in range(len(nbs)):
                res_list = _calculate_diffs_list(nbs, i)
                if res_list is None:
                    break
                res.append(res_list)
        for i in res:
            ret += i[-1]
    return ret


if __name__ == "__main__":
    print(f"Part 1 example: {part1('example')}")
    print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 result: {part2('example')}")
    print(f"Part 2 result: {part2('input')}")
