def getAns(filePWD):
    return [g + '\n' for g in open(filePWD).read().split('\n\n')]

def one_star(filePWD):
    return sum([(len(set(g)) - 1) for g in getAns(filePWD)])

def getYesQ(g):
    return sum([g.count(q) == (g.count('\n')) for q in set(g) if q != '\n'])

def two_star(filePWD):
    return sum([getYesQ(g) for g in getAns(filePWD)])

if __name__ == '__main__':
    print(one_star("input"))
    print(two_star("input"))
