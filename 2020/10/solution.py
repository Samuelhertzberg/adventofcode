import math 

#Gets the difference from i to i+1 in list
def getDiffList(filePWD):
    adapters = list(map(int, [0] + open(filePWD).read().splitlines()))
    adapters.sort()  # Why doesn't pythons list functions have returns? >:(
    adapters.append(adapters[-1] + 3)
    return [b - a for (a, b) in list(zip(adapters, adapters[1:]))]

# Splits the diffs list on [1,3] and returns the sublists lengths: [1,1,1,3,1,1,3,1] => [[1,1],[1],[1]] => [2,1,1]
def getPrunables(diffs):
    threes = [i for i, e in enumerate(diffs) if e == 3]
    zones = list(zip([-1] + threes, threes + [len(diffs)])) #[(i, j),...] where i and j are indexes of last 3 and next 3 respectively 
    return [j-i-2 for (i,j) in zones if i + 1 < j] #Get length of sublists of consecutive ones minus one

#Calcs number of permutations of a binary list without three consecutive zeroes
def getBinPerm(tgt, i, j, curr):
    if(tgt <= curr): #End of recursion
        return 1 if tgt == curr else 0
    if(i == j == 0): #Next number has to be 1
        return getBinPerm(tgt, j, 1, curr + 1 )
    return getBinPerm(tgt, j, 0, curr + 1) + getBinPerm(tgt, j, 1, curr + 1)

def one_star(filePWD):
    diffs = getDiffList(filePWD)
    return diffs.count(1) * (diffs.count(3))

def two_star(filePWD):
    diffs = getDiffList(filePWD)
    prunables = getPrunables(diffs)
    perms = [getBinPerm(l, -1, -1, 0) for l in getPrunables(diffs)]
    prod = 1
    for perm in perms:
       prod *= perm
    return(prod)

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
