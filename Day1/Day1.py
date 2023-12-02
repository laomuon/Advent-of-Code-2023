import re

word_to_check = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def part_1(filename):
    sum = 0
    reg_ex = r'\d'
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            res = re.findall(reg_ex, line)
            sum += int(res[0])*10 + int(res[-1])
    return sum


def part_2(filename):
    sum = 0
    reg_ex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            res = re.findall(reg_ex, line)
            try:
                sum += int(res[0])*10
            except ValueError:
                sum += word_to_check[res[0]]*10
            try:
                sum += int(res[-1])
            except ValueError:
                sum += word_to_check[res[-1]]
    return sum


if __name__ == "__main__":
    print(f"Part 1 example: {part_1('example')}")
    print(f"Part 1 result: {part_1('input')}")
    print(f"Part 2 example: {part_2('example2')}")
    print(f"Part 2 result: {part_2('input')}")
