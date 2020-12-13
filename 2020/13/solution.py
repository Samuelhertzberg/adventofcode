def one_star(filePWD):
    with open(filePWD) as f:
        i = int(f.readline())
        ids = [int(e) for e in f.readline().split(",") if e.isnumeric()]
        waits = [e - (i % e) for e in ids]
        minWait = min(waits)
        bus = ids[waits.index(minWait)]
        return (bus*minWait)

def two_star(filePWD):
    with open(filePWD) as f:
        f.readline()
        ids = [(i, int(e)) for i, e in enumerate(f.readline().split(",")) if e.isnumeric()]
        step = 1
        n = 0
        iters = 0
        for offset, bus in ids:
            while((bus - (n % bus)) % bus != offset % bus):
                n += step
                iters += 1
            step *= bus
        return n

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
