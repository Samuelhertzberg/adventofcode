def bingo(board):
    c = [[row[i] for row in board] for i in range(5)]
    return len(filter(lambda arr: arr.count('X') == 5, (c + board))) > 0

def replace(board, num):
    return [['X' if i == num else i for i in row] for row in board]

def calcScore(board, lastnum):
    return sum([int(i) for i in [n for row in board for n in row] if i != 'X']) * lastnum

def one_star(data):
    return getWinners(data)[0]

def two_star(data):
    return getWinners(data)[-1]

def getWinners(data):
    winners = []
    for n in data['numbers']:
        for i, board in enumerate(data['boards']):
            if(bingo(board)):
                continue
            checkedBoard = replace(board, str(n))
            data['boards'][i] = checkedBoard
            if(bingo(checkedBoard)):
                winners.append(calcScore(checkedBoard, n))
    return winners

def parseData(f):
    f.seek(0)
    chunks = f.read().split('\n\n')
    numbers = map(int, chunks[0].split(','))
    boards = [[r.split() for r in i.split("\n")] for i in chunks[1:]]
    return {'numbers': numbers, 'boards': boards}

if __name__ == '__main__':
    with open('input') as f:
        print(one_star(parseData(f)))
        print(two_star(parseData(f)))
