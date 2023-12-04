import sys


def solution(input):
    lines = input.splitlines()
    numbers = [[c for c in line if c.isdigit()] for line in lines]
    numbers = [int(i[0] + i[-1]) for i in numbers]
    return sum(numbers)


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(solution(input))
