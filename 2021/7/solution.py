def getAlignment(data, fuel):
    return min([sum([fuel(d, c) for d in data]) for c in range(min(data), max(data))])
    
def one_star(data):
    return getAlignment(data, lambda a, b: abs(a - b))

def two_star(data):
    return getAlignment(data, lambda a, b: (1 + abs(a-b))*abs(a-b)/2)

def parseData(f):
    return list(map(int, f.read().split(',')))

if __name__ == '__main__':
    with open('input') as f:
        data = parseData(f)
        print(one_star(data))
        print(two_star(data))
