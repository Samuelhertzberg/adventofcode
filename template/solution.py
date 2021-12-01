def one_star(filePWD):
    with open(filePWD) as f:
        return "todo one star"

def two_star(filePWD):
    with open(filePWD) as f:
        return "todo two star"

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
