import math
def parseFile(filePWD):
    tiles = {}
    tops = {}
    lefts = {}
    rights = {}
    bots = {}
    with open(filePWD) as f:
        r = ":)"
        while(r):
            tileId = int(f.readline()[:-2].split(' ')[1])
            tile = f.read(110)
            top = tile[:10]
            bot = tile[99:-1]
            left = ''.join([tile[i] for i in range(len(tile)) if i % 11 == 0])
            right = ''.join([tile[i+9] for i in range(len(tile)) if i % 11 == 0])
            tiles[tileId] = [right, top, left, bot]
            rots = getRotations([right, top, left, bot])
            for i, r in enumerate(rots):
                addOrUpdate(rights, r[0], (i, tileId))
                addOrUpdate(tops, r[1], (i, tileId))
                addOrUpdate(lefts, r[2], (i, tileId))
                addOrUpdate(bots, r[3], (i, tileId))

            r = f.readline()
        return tiles, tops, lefts, rights, bots

def getRotations(t):
    return [
        [t[0], t[1], t[2], t[3]],
        [t[3][::-1], t[0], t[1][::-1], t[2]],
        [t[2][::-1], t[3][::-1], t[0][::-1], t[1][::-1]],
        [t[1], t[2][::-1], t[3], t[0][::-1]]
    ]

def addOrUpdate(d, k, v):
    if(k in d):
        d[k].append(v)
    else:
        d[k] = [v]

def getTile(g, x, y):
    if(0 <= x < len(g[0]) and 0 <= y < len(g)):
        return g[y][x]
    return (-2, 0, ["", "", "", ""])

def fits(t, nei):
    for i, rot in enumerate(getRotations(t)):
        if(nei[0][0] > 0 and rot[0] != nei[0][2][2]):
            continue
        if(nei[1][0] > 0 and rot[1] != nei[1][2][3]):
            continue
        if(nei[2][0] > 0 and rot[2] != nei[2][2][0]):
            continue
        if(nei[3][0] > 0 and rot[3] != nei[3][2][1]):
            continue
        return i
    return -1

def rPrint(string, depth):
    print("| "*depth, end="")
    print(string)

def getPrettyGrid(g):
    ret  = ""
    for r in g:
        for x in r:
            ret += str(x[0]) + " "
    return ret

def placeTiles(placed, grid, data, x, y, depth):
    if(placed == None):
        return None, None
    
    rPrint(placed, depth)
    rPrint(str(x) + ", " + str(y), depth)
    nei = [getTile(grid, x + xd, y + yd) for xd, yd in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    rPrint(getPrettyGrid(grid), depth)
    avTiles = [(i, data["tiles"][i]) for i in set(data["tiles"].keys()).difference(placed)]
    posTiles = [(i, fits(t, nei), t) for i, t in avTiles if fits(t, nei) >= 0]
    for t in posTiles:
        recGrid = [list(r) for r in grid]
        recGrid[y][x] = t
        recPlaced = set(placed)
        recPlaced.add(t[0])
        rPrint("Testing: ", depth)
        rPrint(getPrettyGrid(recGrid), depth)
        if(nei[0][0] != -2 and grid[y][x+1][0] == -1): #right
            rPrint("going right", depth)
            recPlaced, recGrid = placeTiles(recPlaced, recGrid, data, x+1, y, depth + 1)
        if(nei[1][0] != -2 and recGrid and recGrid[y][x-1][0] == -1):  # left
            rPrint("going left", depth)
            recPlaced, recGrid = placeTiles(recPlaced, recGrid, data, x-1, y, depth + 1)
        if(nei[2][0] != -2 and recGrid and recGrid[y+1][x][0] == -1):  # down
            rPrint("going down", depth)
            recPlaced, recGrid = placeTiles(recPlaced, recGrid, data, x, y+1, depth + 1)
        if(nei[3][0] != -2 and recGrid and recGrid[y-1][x][0] == -1):  # up
            rPrint("going up", depth)
            recPlaced, recGrid = placeTiles(recPlaced, recGrid, data, x, y-1, depth + 1)
        if(recPlaced):
            rPrint("Found suitable at: " + str(x) + ", " + str(y) + ": " + str(t[0]), depth)
            rPrint(getPrettyGrid(grid), depth)
            return recPlaced, recGrid
    rPrint("Nothing suitable at: " + str(x) + ", " + str(y), depth)
    return None, None
    
        
def one_star(filePWD):
    tiles, tops, lefts, rights, bots = parseFile(filePWD)
    data = {"tiles": tiles, "tops": tops, "bots": bots, "lefts": lefts, "rights": rights, }
    n = int(math.sqrt(len(tiles.keys())))
    grid = [[(-1, 0, ["", "", "", ""]) for _ in range(n)] for _ in range(n)]
    placed = set()
    p, g = placeTiles(placed, grid, data, 0, 0, 0)
    print(p)
    print(g)
    print((tiles[2][0], 0, tiles[2][1]))
    nei = [(-2, 0, ["", "", "", ""]), (-1, 0, ["", "", "", ""]), (-2, 0, ["", "", "", ""]), (2, 0, tiles[2])]
    print(fits(tiles[3][2], nei))

def two_star(filePWD):
    with open(filePWD) as f:
        return "todo two star"

if __name__ == '__main__':
    print(one_star('input_short'))
    print(two_star('input'))
