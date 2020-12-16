def crunch(filePWD):
    with open(filePWD) as f:
        l = f.readline()
        ranges = []
        while(l != "\n"):
           rangePair = l.split(": ")[1].split(" or ")
           range1 = rangePair[0].split("-")
           range1 = range(int(range1[0]), int(range1[1]) + 1)
           range2 = rangePair[1].split("-")
           range2 = range(int(range2[0]), int(range2[1]) + 1)
           ranges.append((l.split(": ")[0], range1, range2)) 
           l = f.readline()
           
        f.readline()
        myTicket = [int(v) for v in f.readline().split(",")]
        f.readline()
        f.readline()
        tickets = [[int(v) for v in r.split(',')] for r in f.read().splitlines()]
        errRate = 0
        fields = set([f for f,_,_ in ranges])
        possibleFields = [fields.copy() for _ in range(len(tickets[0]))]
        for ticket in tickets:
            for i, v in enumerate(ticket):
                pos = getPosFields(v, ranges)
                if(len(pos) <= 0):
                    errRate += v
                    continue
                possibleFields[i] = possibleFields[i].intersection(pos)
        actualFields = sieve(possibleFields)
        prod = 1
        for i, field in enumerate(actualFields):
            if(field.startswith("departure")):
                prod *= myTicket[i]
        return errRate, prod

def sieve(fields):
    while(any([len(f)>1 for f in fields])):
        for posf in fields:
            if(len(posf) == 1):
                field = posf.pop()
                for f in fields:
                    f.discard(field)
                posf.add(field)
    return [f.pop() for f in fields]

def getPosFields(v, ranges):
    retur = set()
    for field, r1, r2 in ranges:
        if(v in r1 or v in r2):
            retur.add(field)
    return retur

if __name__ == '__main__':
    oneStar, twoStar = crunch('input')
    print(oneStar)
    print(twoStar)
