def parse(expr):
    retur = []
    i = 0
    while(i < len(expr)):
        c = expr[i]
        if(c.isdigit()):
            retur.append(("val", int(c)))
        elif(c == "+" or c == "*"):
            retur.append(("op", c))
        elif(c == "("):
            i += 1
            p = 1
            t = i
            while(i < len(expr) and 0 < p):
                p += 1 if expr[i] == "(" else (-1 if expr[i] == ")" else 0)
                i += 1
            retur.append(("expr", parse(expr[t:i-1])))
        else:
            pass
        i += 1
    return retur

def val(token, advanced):
    t, val = token
    return (t, eval(val, advanced)) if t == "expr" else token

def eval(seq, advanced):
    if(len(seq) == 1):
        return val(seq[0], advanced)[1]
    i = 1
    if(advanced):
        p = ("op", "+")
        m = ("op", "*")
        i = seq.index(p) if p in seq else seq.index(m)

    at, A = val(seq[i-1], advanced)
    bt, B = val(seq[i], advanced)
    ct, C = val(seq[i+1], advanced)
    seq[i-1:i+2] = [("val", {"+": A + C, "*": A * C}[B])]

    return eval(seq, advanced)

def one_star(filePWD):
    with open(filePWD) as f:
        return sum([eval(parse(row), False) for row in f.read().splitlines()])

def two_star(filePWD):
    with open(filePWD) as f:
        return sum([eval(parse(row), True) for row in f.read().splitlines()])

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
