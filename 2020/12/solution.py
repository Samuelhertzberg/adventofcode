import math
def one_star(filePWD):
    with open(filePWD) as f:
        p = [0,0]
        d = 0
        ds = ([1, 0], [0, -1], [-1, 0], [0, 1])
        instructions = {
            "N": lambda imm: ([p[0], p[1] + imm], d),
            "S": lambda imm: ([p[0], p[1] - imm], d),
            "E": lambda imm: ([p[0] + imm, p[1]], d),
            "W": lambda imm: ([p[0] - imm, p[1]], d),
            "L": lambda imm: (p, (d - int(imm/90)) % 4),
            "R": lambda imm: (p, (d + int(imm/90)) % 4),
            "F": lambda imm: ([p[0] + ds[d][0]*imm, p[1] + ds[d][1]*imm], d)
        }
        for instruction in f.readlines():
            op = instruction[0]
            imm = int(instruction[1:])
            p, d = instructions[op](imm)
        return sum(map(abs, p))

def getTurn(x, y, turns, direction):
    for i in range(turns):
        x_t = x
        x = direction * y
        y = - direction * x_t
    return [x,y]

def two_star(filePWD):
    with open(filePWD) as f:
        p = [0, 0]
        d = [10, 1]
        instructions = {
            "N": lambda imm: (p, [d[0], d[1] + imm]),
            "S": lambda imm: (p, [d[0], d[1] - imm]),
            "E": lambda imm: (p, [d[0] + imm, d[1]]),
            "W": lambda imm: (p, [d[0] - imm, d[1]]),
            "L": lambda imm: (p, getTurn(d[0], d[1], int(imm/90), -1)),
            "R": lambda imm: (p, getTurn(d[0], d[1], int(imm/90), 1)),
            "F": lambda imm: ([p[0] + d[0] * imm, p[1] + d[1] * imm], d)
        }
        for instruction in f.readlines():
            op = instruction[0]
            imm = int(instruction[1:])
            p, d = instructions[op](imm)
        return sum(map(abs, p))

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
