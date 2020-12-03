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

def short1():
    return len([l for i, l in enumerate(open('input').readlines()) if l[(i*3) % (len(l) - 1) ] == '#'])

def short2(vec):
    return len([l for i, l in enumerate(open('input').readlines()) if i % vec[1] == 0 and l[int(i*vec[0]/vec[1]) % (len(l) - 1) ] == '#'])

def arvids():
    print(sum([(l[i*3 % len(l)] == '#') for i, l in enumerate(open('input').read().splitlines())]))

        

if __name__ == '__main__':
    print(solution([1,1])*solution([3,1])*solution([5,1])*solution([7,1])*solution([1,2]))
    print(solution([3,1]))
    print(short1())

    print(solution([3,2]))
    print(short2([3,2]))
    
    