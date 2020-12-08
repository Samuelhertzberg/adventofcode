def parse(filePWD):
    with open(filePWD) as f:
        return [[line.split()[0], int(line.split()[1])]
                for line in f.read().splitlines()]

def execute(code, skip):
    seen = {}
    acc = 0
    i = 0
    jmps = []
    while(i < len(code)):
        if(i in seen):
            return {"acc": acc, "path": jmps, "term": False}
        seen[i] = True
        if(code[i][0] == "acc"):
            acc += code[i][1]
        elif(code[i][0] == "jmp" and i != skip):
            jmps.append(i)
            i += (code[i][1] if (code[i][1] < 0) else code[i][1]) - 1
        i+=1
    return {"acc": acc, "path": jmps, "term": True}

        
def one_star(code):
    return execute(code, -1)["acc"]

def two_star(code):
    res = execute(code, -1)
    jmpskip = [jmp for jmp in res["path"] if execute(code, jmp)["term"]][0]
    return execute(code, jmpskip)["acc"]


if __name__ == '__main__':
    code = parse('input')
    print(one_star(code))
    print(two_star(code))
