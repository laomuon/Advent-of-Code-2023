def part1(filename: str) -> int:
    ret = 0
    empty_line = []
    empty_col = []
    galaxies = []
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if len(empty_col) == 0:
                empty_col = [i for i in range(len(line.replace("\n", "")))]
            if '#' not in line:
                empty_line.append(i)
            else:
                for j, pt in enumerate(line):
                    if pt == '#':
                        galaxies.append((i, j))
                        if j in empty_col:
                            empty_col.remove(j)

        for i, galaxy in enumerate(galaxies):
            line, col = galaxy
            for j in empty_line:
                if j < line:
                    galaxies[i] = (galaxies[i][0]+1, galaxies[i][1])

            for j in empty_col:
                if j < col:
                    galaxies[i] = (galaxies[i][0], galaxies[i][1]+1)

    while len(galaxies)>0:
        galaxy = galaxies.pop(0)
        for g in galaxies:
            ret += abs(g[0]-galaxy[0]) + abs(g[1]-galaxy[1])
    return ret


def part2(filename: str) -> int:
    ret = 0
    empty_line = []
    empty_col = []
    galaxies = []
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if len(empty_col) == 0:
                empty_col = [i for i in range(len(line.replace("\n", "")))]
            if '#' not in line:
                empty_line.append(i)
            else:
                for j, pt in enumerate(line):
                    if pt == '#':
                        galaxies.append((i, j))
                        if j in empty_col:
                            empty_col.remove(j)

        for i, galaxy in enumerate(galaxies):
            line, col = galaxy
            for j in empty_line:
                if j < line:
                    galaxies[i] = (galaxies[i][0]+999999, galaxies[i][1])

            for j in empty_col:
                if j < col:
                    galaxies[i] = (galaxies[i][0], galaxies[i][1]+999999)

    while len(galaxies)>0:
        galaxy = galaxies.pop(0)
        for g in galaxies:
            ret += abs(g[0]-galaxy[0]) + abs(g[1]-galaxy[1])
    return ret


if __name__ == "__main__":
    print(f"Part 1 example: {part1('example')}")
    print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 result: {part2('example')}")
    print(f"Part 2 result: {part2('input')}")
