def interpolate(x1, y1, x2, y2, allowDiagonals=False):
    if x1 == x2:
        return [(x1, i + min(y1, y2)) for i in range(abs(y1 - y2) + 1)]
    elif y1 == y2:
        return [(i + min(x1, x2), y1) for i in range(abs(x1 - x2) + 1)]
    elif allowDiagonals and abs(x1 - x2) == abs(y1 - y2):
        xDir = 1 if x1 < x2 else -1
        yDir = 1 if y1 < y2 else -1
        return list(zip(list(range(x1, x2 + xDir, xDir)), list(range(y1, y2 + yDir, yDir))))
    else:
        return []

def getCoveredMap(lines, includeDiagonals=False):
    covered = {}
    for line in lines:
        points = interpolate(
            line['x1'], line['y1'],
            line['x2'], line['y2'],
            includeDiagonals
        )
        for point in points:
            if point not in covered:
                covered[point] = 1
            else:
                covered[point] += 1
    return covered

def one_star(data):
    covered = getCoveredMap(data)
    return len(list(covered.values())) - list(covered.values()).count(1)
    
def two_star(data):
    covered = getCoveredMap(data, True)
    return len(list(covered.values())) - list(covered.values()).count(1)

def parseData(f):
    lines = []
    for line in f.read().split('\n'):
        pairs = [p.split(',') for p in line.split(' -> ')]
        lines.append({'x1': int(pairs[0][0]), 'y1': int(pairs[0][1]), 'x2': int(pairs[1][0]), 'y2': int(pairs[1][1])})
    return lines

if __name__ == '__main__':
    with open('input') as f:
        data = parseData(f)
        print(one_star(data))
        print(two_star(data))
