def one_star(instr):
    dInstr = [int(l[1]) for l in instr if l[0] == 'down']
    upInstr = [-int(l[1]) for l in instr if l[0] == 'up']
    fInstr = [int(l[1]) for l in instr if l[0] == 'forward']
    vInstr = dInstr + upInstr
    return (sum(vInstr)) * sum(fInstr)


def two_star(instr):
    a = 0
    x = 0
    d = 0
    for i in instr:
        if i[0] == 'up':
            a = a - int(i[1])
        elif i[0] == 'down':
            a = a + int(i[1])
        elif i[0] == 'forward':
            x = x + int(i[1])
            d = d + a * int(i[1])
    return x * d

def parse_input(f):
    lines = f.readlines()
    lines = [line.split() for line in lines]
    return lines

if __name__ == '__main__':
    with open('input') as f:
        instr = parse_input(f)
        print(one_star(instr))
        print(two_star(instr))
