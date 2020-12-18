def getNeighbours(c, dim):
    ox,oy,oz,ow = c
    ni = [-1,0,1]
    n = []
    for z in ni:
        for y in ni:
            for x in ni:
                for w in (ni if dim else [0]):
                    if((x, y, z, w) != (0, 0, 0, 0)):
                        n.append((ox + x, oy + y, oz + z, ow + w))                
    return n

def eval(m, c, nei):
    n = sum([m[k] for k in nei if k in m])
    if(c in m and m[c]):
        return 1 < n < 4
    else:
        return n == 3

def crunch(filePWD, dim):
    m = {}
    with open(filePWD) as f:
        for y, row in enumerate(f.read().splitlines()):
            for x, c in enumerate(row):
                m[(x,y,0,0)] = (c == '#')

    for _ in range(6):
        m_new = {}
        for cube in m.keys():
            m_new[cube] = False
            for adj in getNeighbours(cube, dim):
                m_new[adj] = False
        for cube in m_new.keys():
            m_new[cube] = eval(m, cube, getNeighbours(cube, dim))
        m = dict(m_new)
    return sum([m[k] for k in m.keys()])

def two_star(filePWD):
    with open(filePWD) as f:
        return "todo two star"

if __name__ == '__main__':
    print(crunch('input', False))
    print(crunch('input', True))
