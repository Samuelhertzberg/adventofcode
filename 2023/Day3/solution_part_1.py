import sys
import re


def getNumbersOnLine(numbers, x):
    return [int(m.group()) for m in numbers if m.start() - 1 <= x <= m.end()]


def getNumbers(numbers, x, y):
    return (
        getNumbersOnLine(numbers[y], x)
        + (getNumbersOnLine(numbers[y - 1], x) if y > 0 else [])
        + (getNumbersOnLine(numbers[y + 1], x) if y < len(numbers) - 1 else [])
    )


def solution(input):
    lines = input.splitlines()
    numbers = [list(re.finditer(r"\d+", line)) for line in lines]
    items = [list(re.finditer(r"[^0-9.]", line)) for line in lines]

    itemIds = []
    for y, line in enumerate(items):
        for itemMatch in line:
            itemIds = itemIds + getNumbers(numbers, itemMatch.start(), y)

    return sum(itemIds)


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(solution(input))
