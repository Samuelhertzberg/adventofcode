def oob(seats, x, y):
    return not (0 <= x < len(seats[0]) and 0 <= y < len(seats))

def state_next(seats, x, y, lim, threshhold):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0),(1, 0), (-1, 1), (0, 1), (1, 1)]
    n = [getFirstSeat(seats, x, y, xd, yd, lim) for (xd, yd) in dirs]
    retur = {".": ".",
             "L": "#" if n.count("#") == 0 else "L",
             "#": "L" if n.count("#") >= threshhold else "#"}
    return retur[seats[y][x]]

def getFirstSeat(seats, x, y, xd, yd, lim):
    c = '.'
    i = 1
    while(c == '.' and i <= lim and not oob(seats, x+xd*i, y+yd*i)):
        c = seats[y+yd*i][x+xd*i]
        i += 1
    return c

def run(filePWD, lim=1, threshhold=4):
    with open(filePWD) as f:
        seats = [[("." if p == "." else '#') for p in row] for row in f.read().splitlines()]
        rows = len(seats)
        cols = len(seats[0])
        seats_next = [[state_next(seats, x, y, lim, threshhold) for x in range(cols)] for y in range(rows)]
        while(seats != seats_next):
            seats = seats_next
            seats_next = [[state_next(seats, x, y, lim, threshhold) for x in range(cols)] for y in range(rows)]
        return sum([row.count("#") for row in seats])

if __name__ == '__main__':
    print(run('input')) #one star
    print(run('input', 1000, 5)) #two star
