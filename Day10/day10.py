import sys

sys.setrecursionlimit(100000000)
# 1-east  -2-south  -1-west  2-north
MAP_PIPE = {
    "|": (2, -2),
    "-": (1, -1),
    "L": (2, 1),
    "J": (2, -1),
    "7": (-2, -1),
    "F": (-2, 1),
    ".": None,
    "S": ()
}


MAP = []


MAIN_LOOP = []


def check_correct(pos, orientation):
    try:
        if orientation == 1:
            end = MAP[pos[0]][pos[1]+1]
            if end is not None and any([o == -orientation for o in MAP_PIPE[end]]):
                next_o = [o for o in MAP_PIPE[end] if o != - orientation][0]
                return (pos[0], pos[1]+1, next_o)
    except IndexError:
        pass

    try:
        if orientation == -1:
            end = MAP[pos[0]][pos[1]-1]
            if end is not None and any([o == -orientation for o in MAP_PIPE[end]]):
                next_o = [o for o in MAP_PIPE[end] if o != - orientation][0]
                return (pos[0], pos[1]-1, next_o)
    except IndexError:
        pass

    try:
        if orientation == 2:
            end = MAP[pos[0]-1][pos[1]]
            if end is not None and any([o == -orientation for o in MAP_PIPE[end]]):
                next_o = [o for o in MAP_PIPE[end] if o != - orientation][0]
                return (pos[0]-1, pos[1], next_o)
    except IndexError:
        pass
    try:
        if orientation == -2:
            end = MAP[pos[0]+1][pos[1]]
            if end is not None and any([o == -orientation for o in MAP_PIPE[end]]):
                next_o = [o for o in MAP_PIPE[end] if o != - orientation][0]
                return (pos[0]+1, pos[1], next_o)
    except IndexError:
        pass
    return None


def find_next_pipe(start: str, pos, count, connect_orientation=None):
    if connect_orientation is None:
        for o in [1, -1, 2, -2]:
            next_pos = check_correct(pos, o)
            if next_pos is not None:
                count += 1
                return find_next_pipe(MAP[next_pos[0]][next_pos[1]], (next_pos[0], next_pos[1]), count, next_pos[2])
    next_pos = check_correct(pos, connect_orientation)
    if next_pos is not None:
        MAIN_LOOP.append((next_pos[0], next_pos[1]))
        next_pipe = MAP[next_pos[0]][next_pos[1]]
        count += 1
        return find_next_pipe(next_pipe, (next_pos[0], next_pos[1]), count, next_pos[2])
    count += 1
    return count


def part1(filename: str) -> int:
    ret = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            MAP.append([p for p in line.replace("\n", "")])
            if "S" in line:
                starting_pos = (len(MAP)-1, line.index("S"))

        ret = find_next_pipe("S", starting_pos, ret)
        return ret/2


def part2(filename: str) -> int:
    ret = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            MAP.append([p for p in line.replace("\n", "")])
            if "S" in line:
                starting_pos = (len(MAP)-1, line.index("S"))
                MAIN_LOOP.append((starting_pos[0], starting_pos[1]))

        find_next_pipe("S", starting_pos, ret)
        for i, line in enumerate(MAP):
            inside = False
            for j, p in enumerate(line):
                if p in ['|', 'J', 'L'] and (i, j) in MAIN_LOOP:
                    inside = not inside
                if inside and (i, j) not in MAIN_LOOP:
                    ret += 1

        return ret


if __name__ == "__main__":
    # print(f"Part 1 example: {part1('example2')}")
    # print(f"Part 1 result: {part1('input')}")
    # print(f"Part 2 result: {part2('example3')}")
    print(f"Part 2 result: {part2('input')}")
