def solution(vec):
    with open('input') as f:
        row = f.readline()
        rowLen = len(row) - 1
        pos = 0
        trees = 0
        while row:
            if(row[pos % rowLen] == '#'):
                trees += 1
            for _ in range(vec[1]):
                if(row):
                    row = f.readline()
            pos += vec[0] 
        return trees

if __name__ == '__main__':
    print(solution([3,1]))
    print(solution([1,1])*solution([3,1])*solution([5,1])*solution([7,1])*solution([1,2]))
    
    