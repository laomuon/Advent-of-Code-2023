import re


def part1(filename: str) -> int:
    ret = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            ret_line = 0
            line_items = re.split(r'\s+', line)
            nb_items = len(line_items)
            if nb_items == 2:
                continue
            sep_idx = line_items.index('|')
            for win_nb in line_items[sep_idx+1:-1]:
                if win_nb in line_items[2:sep_idx]:
                    if ret_line == 0:
                        ret_line = 1
                    else:
                        ret_line *= 2
            ret += ret_line

    return ret


def part2(filename: str) -> int:
    ret = 0
    lines_items = []
    card_numbers = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            item = re.split(r'\s+', line)
            nb_items = len(item)
            if nb_items == 2:
                continue
            lines_items.append(item)
            card_numbers.append(1)

    for i, line in enumerate(lines_items):
        counter = 0
        sep_idx = line.index('|')
        for win_nb in line[sep_idx+1:-1]:
            if win_nb in line[2:sep_idx]:
                counter += 1
        if counter > 0:
            for j in range(i+1, i+counter+1):
                card_numbers[j] += card_numbers[i]

    for nb in card_numbers:
        ret += nb

    return ret


if __name__ == "__main__":
    print(f"Part 1 example: {part1('example')}")
    print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 result: {part2('example')}")
    print(f"Part 2 result: {part2('input')}")
