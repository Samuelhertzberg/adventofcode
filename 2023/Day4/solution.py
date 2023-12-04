import sys

def getNumberOfWins(line):
    parts = line.split(": ")[1].split(" | ")
    winners = set(parts[0].split(" "))
    actual = set(parts[1].split(" "))
    return len(winners.intersection(actual))

def parse(input):
    lines = input.replace("  ", " ").splitlines()
    return [getNumberOfWins(line) for line in lines]

def part1(input):
    winners = parse(input)
    return sum([2 ** (i - 1) for i in winners if i > 0])

def part2(input):
    winners = parse(input)
    generatedCards = []
    for wins in reversed(winners):
        children = generatedCards[:wins]
        generatedCards.insert(0, sum(children) + 1)
    return sum(generatedCards)

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(part1(input))
        print(part2(input))
