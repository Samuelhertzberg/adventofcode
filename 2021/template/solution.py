def one_star(data):
    return "todo"

def two_star(data):
    return "todo"

def parseData(f):
    return "todo"

if __name__ == '__main__':
    with open('input') as f:
        data = parseData(f)
        print(one_star(data))
        print(two_star(data))
