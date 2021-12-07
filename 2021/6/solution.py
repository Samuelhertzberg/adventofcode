dynMap = {}

def getDescendants(currCycle, gens):
    if((currCycle, gens) in dynMap):
        return dynMap[(currCycle, gens)]
    elif gens <= 0:
        return 1
    elif currCycle == 0:
        r = getDescendants(6, gens - 1) + getDescendants(8, gens - 1)
    else:
        r = getDescendants(currCycle - 1, gens - 1)
    dynMap[(currCycle, gens)] = r
    return r

def one_star(data):
    return sum([getDescendants(n, 80) for n in data])

def two_star(data):
    return sum([getDescendants(n, 256) for n in data])

def parseData(f):
    return list(map(int,f.read().split(',')))

if __name__ == '__main__':
    with open('input') as f:
        data = parseData(f)
        print(one_star(data))
        print(two_star(data))
