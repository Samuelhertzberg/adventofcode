import sys


def maxVal(game, color):
    return max([int(draw[0]) for draw in game if draw[1] == color])


def solution(input):
    games = [line.split(":")[1] for line in input.splitlines()]
    games = [game.replace(";", ",").split(",") for game in games]
    games = [[draw.strip().split(" ") for draw in game] for game in games]
    return sum(
        [maxVal(g, "red") * maxVal(g, "green") * maxVal(g, "blue") for g in games]
    )


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(solution(input))
