def check_vertical_line(pattern):
    for i in range(1, len(pattern)):
        j = 1
        if pattern[i] != pattern[i-1]:
            continue
        while (i+j < len(pattern) and i-j-1 >= 0):
            if pattern[i+j] != pattern[i-j-1]:
                break
            j += 1
        else:
            return i
    return 0


def check_horizontal_line(pattern):
    cols_count = len(pattern[0])
    transposed = []
    for i in range(cols_count):
        transposed_line = ""
        for line in pattern:
            transposed_line += line[i]
        transposed.append(transposed_line)
    return check_vertical_line(transposed)


def check_smudge_vertical(pattern):
    for i in range(1, len(pattern)):
        j = 1
        smudged = False
        if pattern[i] != pattern[i-1]:
            if len([k for k in range(len(pattern[i])) if pattern[i][k] != pattern[i-1][k]]) > 1:
                continue
            smudged = True
        while (i+j < len(pattern) and i-j-1 >= 0):
            if pattern[i+j] != pattern[i-j-1]:
                if smudged:
                    break

                if len([k for k in range(len(pattern[i+j])) if pattern[i+j][k] != pattern[i-j-1][k]]) > 1:
                    break
                smudged = True
            j += 1
        else:
            if smudged:
                return i
    return 0


def check_smudge_horizontal(pattern):
    cols_count = len(pattern[0])
    transposed = []
    for i in range(cols_count):
        transposed_line = ""
        for line in pattern:
            transposed_line += line[i]
        transposed.append(transposed_line)
    return check_smudge_vertical(transposed)


def part1(filename: str) -> int:
    patterns = []
    i_p = 0
    ret = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '#' not in line and '.' not in line:
                i_p += 1
                continue
            try:
                patterns[i_p].append(line.replace("\n", ""))
            except IndexError:
                patterns.append([line.replace("\n", "")])

    for pattern in patterns:
        ret += check_horizontal_line(pattern) + 100 * check_vertical_line(pattern)

    return ret


def part2(filename: str) -> int:
    patterns = []
    i_p = 0
    ret = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '#' not in line and '.' not in line:
                i_p += 1
                continue
            try:
                patterns[i_p].append(line.replace("\n", ""))
            except IndexError:
                patterns.append([line.replace("\n", "")])

    for pattern in patterns:
        ret += check_smudge_horizontal(pattern) + 100 * check_smudge_vertical(pattern)

    return ret

if __name__ == "__main__":
    print(f"Part 1 example: {part1('example')}")
    print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 result: {part2('example')}")
    print(f"Part 2 result: {part2('input')}")
