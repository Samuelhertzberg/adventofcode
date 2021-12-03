def getValue(lines, v):
    transpose = [[line[i] for line in lines] for i in range(len(lines[0]))]
    d2 = ''.join(['1' if i.count(v) > len(i)/2 else '0' for i in transpose])
    return int(d2, 2)

def one_star(lines):
    return getValue(lines, '1') * getValue(lines, '0')

def getAtmoStatus(lines, minOrMax, precedence):
    for bi in range(len(lines[0])):
        numbers = [[n for n in lines if n[bi] == v] for v in precedence]
        lines = minOrMax(numbers, key=len)
        if(len(lines) <= 1):
            return int(lines[0], 2)
    
def two_star(lines):
    return getAtmoStatus(lines, max, ['1', '0']) * getAtmoStatus(lines, min, ['0', '1'])
    
if __name__ == '__main__':
    with open('input') as f:
        lines = f.read().split('\n')
        print(one_star(lines))
        print(two_star(lines))
