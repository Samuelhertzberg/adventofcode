import sys
import re


def getNumbersOnLine(numbers, x):
    return [int(m.group()) for m in numbers if m.start() - 1 <= x <= m.end()]


def getNumbers(numbers, x, y):
    numbers = (
        getNumbersOnLine(numbers[y], x)
        + (getNumbersOnLine(numbers[y - 1], x) if y > 0 else [])
        + (getNumbersOnLine(numbers[y + 1], x) if y < len(numbers) - 1 else [])
    )
    return numbers[0] * numbers[1] if len(numbers) == 2 else 0


def solution(input):
    lines = input.splitlines()
    numbers = [list(re.finditer(r"\d+", line)) for line in lines]
    items = [list(re.finditer(r"[*]", line)) for line in lines]

    return sum(
        [
            sum([getNumbers(numbers, itemMatch.start(), y) for itemMatch in line])
            for y, line in enumerate(items)
        ]
    )


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(solution(input))
