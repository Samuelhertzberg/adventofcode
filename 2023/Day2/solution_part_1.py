import sys

allowedDraws = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def drawAllowed(draw):
    draw = draw.strip().split(" ")
    return allowedDraws[draw[1]] >= int(draw[0])


def gameAllowed(game):
    return all([drawAllowed(draw) for draw in game.replace(";", ",").split(",")])


def solution(input):
    games = [line.split(":")[1] for line in input.splitlines()]
    allowedGameIndexes = [i + 1 for i, game in enumerate(games) if gameAllowed(game)]
    return sum(allowedGameIndexes)


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(solution(input))
