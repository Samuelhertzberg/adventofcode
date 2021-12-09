letters = 'abcdefgh'
correctSegments = {'0': 'abcefg', '1': 'cf', '2': 'acdeg', '3': 'acdfg', '4': 'bcdf', '5': 'abdfg', '6': 'abdefg', '7': 'acf', '8': 'abcdefg', '9': 'abcdfg'}

def one_star(data):
    outputs = [l[1] for l in data]
    outputs = [output for sublist in outputs for output in sublist]
    return sum([1 for n in outputs if len(n) in [2, 3, 4, 7]])

def two_star(data):
    ids = generateNumIdentifier()
    numbers = [getNumber(decodeSequence(line[0], ids), line[1]) for line in data]
    return sum(numbers)

def getNumber(key, seq):
    return int(''.join([key[hashable(segments)] for segments in seq]))

def hashable(s):
    return tuple(sorted(s))

def generateNumIdentifier():
    all = ''.join(correctSegments.values())
    ids = {hashable(map(all.count, segments)): n
           for (n, segments) in correctSegments.items()}
    return ids

def decodeSequence(sequence, numberIdentifiers):
    key = {}
    all = ''.join(sequence)
    for segments in sequence:
        id = hashable(map(all.count, segments))
        if id in numberIdentifiers:
            key[hashable(segments)] = numberIdentifiers[id]
    return key

def parseData(f):
    lines = f.read().split('\n')
    lines = map(lambda x: x.split(' | '), lines)
    lines = [[l[0].split(), l[1].split()] for l in lines]
    return lines

if __name__ == '__main__':
    with open('input') as f:
        data = parseData(f)
        print(one_star(data))
        print(two_star(data))
