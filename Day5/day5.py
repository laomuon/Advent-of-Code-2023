import re
import typing as T


def _check_next_step(source: int, convert_lists: T.List, index: int = 0) -> int:
    try:
        convert_list = convert_lists[index]
    except IndexError:
        return source
    for dest, start, nb_range in convert_list:
        if source in range(start, start + nb_range):
            return _check_next_step(dest + source - start, convert_lists, index + 1)
    return _check_next_step(source, convert_lists, index + 1)


def intersect(a, b):
    a_start, a_len = a
    a_end = a_start + a_len
    b_start, b_len = b
    b_end = b_start + b_len

    i_start = max(a_start, b_start)
    i_end = min(a_end, b_end)

    return (i_start, i_end - i_start)


# Range a - Range b
def difference_range(a, b):
    a_start, a_len = a
    a_end = a_start + a_len
    b_start, b_len = b
    b_end = b_start + b_len
    diff = []
    if a_start < b_start:
        diff.append((a_start, b_start - a_start))

    if a_end > b_end:
        diff.append((b_end, a_end - b_end))

    return diff


def _check_next_step2(
    source_list: T.List, convert_lists: T.List, index: int = 0
) -> int:
    try:
        convert_list = convert_lists[index]
    except IndexError:
        return source_list
    output = []
    for dest, start, nb_range in convert_list:
        rest = []
        for source in source_list:
            i_start, i_len = intersect(source, (start, nb_range))
            if i_len > 0:
                output.append((i_start - start + dest, i_len))
                rest += difference_range(source, (start, nb_range))
            else:
                rest.append(source)
        source_list = rest
    return _check_next_step2(output + rest, convert_lists, index + 1)


def part1(filename: str) -> int:
    reg_ex = r"\w+[\d]|[\d]"
    seeds = []
    map = []
    map_index = -1
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            nbs_string = re.findall(reg_ex, line)
            if len(nbs_string) > 0:
                nbs = [int(nb) for nb in nbs_string]
                if len(seeds) == 0:
                    seeds = nbs.copy()
                    continue
                map[map_index].append(nbs.copy())
                continue
            if len(re.findall(r"\w+", line)) > 0:
                map.append([])
                map_index += 1

    ret = []
    for seed in seeds:
        ret.append(_check_next_step(seed, map, 0))

    return min(ret)


def part2(filename: str) -> int:
    reg_ex = r"\w+[\d]|[\d]"
    seeds = []
    map = []
    map_index = -1
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            nbs_string = re.findall(reg_ex, line)
            if len(nbs_string) > 0:
                nbs = [int(nb) for nb in nbs_string]
                if len(seeds) == 0:
                    seeds = nbs.copy()
                    continue
                map[map_index].append(nbs.copy())
                continue
            if len(re.findall(r"\w+", line)) > 0:
                map.append([])
                map_index += 1

    ret = []
    for i in range(len(seeds)):
        if i % 2 == 1:
            ret += _check_next_step2([(seeds[i - 1], seeds[i])], map, 0)

    return min([r[0] for r in ret])


if __name__ == "__main__":
    print(f"Part 1 example: {part1('example')}")
    print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 example: {part2('example')}")
    print(f"Part 2 result: {part2('input')}")
