import sys


def solution(input):
    input = (
        input.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
        .replace("zero", "z0o")
    )
    lines = input.splitlines()
    numbers = [[c for c in line if c.isdigit()] for line in lines]
    numbers = [int(i[0] + i[-1]) for i in numbers]
    return sum(numbers)


if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(solution(input))
