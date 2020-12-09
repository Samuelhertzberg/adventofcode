def checkSum(q, n):
    return any([(n-x) in [y for y in q if x != y] for x in q])

def one_star(filePWD):
    with open(filePWD) as f:
        q = [int(f.readline()) for _ in range(25)]
        n = int(f.readline())
        while(checkSum(q, n)):
            q.pop(0)
            q.append(n)
            n = int(f.readline())
        return n

            
def two_star(filePWD):
    n = one_star(filePWD)
    with open(filePWD) as f:
        q = list(map(int, f.read().splitlines()))
        i = 1
        while(True):
            j = i + 1
            while(sum(q[i:j+1]) <= n):
                if(sum(q[i:j+1]) == n):
                    return min(q[i:j+1]) + max(q[i:j+1])
                j += 1
            i += 1

def two_star_short(filePWD):
    n = one_star(filePWD)
    with open(filePWD) as f:
        q = list(map(int, f.read().splitlines()))
        return [l for l in [[max(l) + min(l) for l in [q[i:j] for j in range(i+2, len(q)+1)] if sum(l) == n] for i in range(len(q)-1)] if l][0][0]


if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
    print(two_star_short('input'))
