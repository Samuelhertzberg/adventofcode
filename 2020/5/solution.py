def index(ind, A, B):
    ind = ind.replace(A, '0').replace(B, '1')
    return int(ind, 2)

def getIds(filePWD):
    with open(filePWD) as f:
       lines = f.read().splitlines()
       getRow = lambda x: index(x[:7],'F','B')
       getCol = lambda x: index(x[-3:],'L','R')
       return [8 * getRow(l) + getCol(l) for l in lines]

def one_star(filePWD):
    return max(getIds(filePWD))

def two_star(filePWD):
    ids = getIds(filePWD)
    return [id+1 for id in ids if (id+2) in ids and (id+1) not in ids][0]

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
