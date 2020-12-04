import re

def readPair(f):
    char = f.read(1)
    if(char == "\n"): #EOL
        return -1
    if(char == ""): #EOF
        return -2
    key = []
    value = []
    while(char != ":"):
        key.append(char)
        char = f.read(1)
    char = f.read(1)
    while(char not in ["", " ", "\n"]):
        value.append(char)
        char = f.read(1)
    return {"key": ''.join(key), "value": ''.join(value)}

def checkIsNumber(n):
    return len(n) if n.isnumeric() else -1

def checkRange(n, minVal, maxVal):
    return minVal <= int(n) and int(n) <= maxVal

def checkYearAndRange(y, minVal, maxVal):
        return checkIsNumber(y) == 4 and checkRange(y, minVal, maxVal)
        

def checkHeight(h):
    unit = h[-2:]
    l = checkIsNumber(h[:-2])
    return (l == 3 and checkRange(h[:-2], 150, 193)) if unit == "cm" else (l == 2 and checkRange(h[:-2], 59, 76))

def checkContent(s, length, allowed):
    for char in s:
        if char not in allowed:
            return False
    return len(s) == length
    

def one_star(filePWD):
    with open(filePWD) as f:
        valid = 0
        while True:
            fields = {"byr": False,"iyr": False,"eyr": False,"hgt": False,"hcl": False,"ecl": False,"pid": False }
            present = 0
            pair = readPair(f)
            while pair not in [-1, -2]:
                key = pair["key"]
                value = pair["value"]
                if(key in fields.keys() and not fields[key]):
                    present += 1
                    fields[key] = True
                pair = readPair(f)
            if(present >= 7):
                valid += 1
            if(pair == -2):
                return valid

def two_star(filePWD):
    with open(filePWD) as f:
        valid = 0
        while True:
            fields = {
                "byr": 
                    {"seen": False, "filter": lambda x: checkYearAndRange(x, 1920, 2002)},
                "iyr": 
                    {"seen": False, "filter": lambda x: checkYearAndRange(x, 2010, 2020)},
                "eyr": 
                    {"seen": False, "filter": lambda x: checkYearAndRange(x, 2020, 2030)},
                "hgt": 
                    {"seen": False, "filter": lambda x: checkHeight(x)},
                "hcl": 
                    {"seen": False, "filter": lambda x: x[:1] == "#" and checkContent(x[1:], 6,"0123456789abcdef")},
                "ecl": 
                    {"seen": False, "filter": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]},
                "pid": 
                    {"seen": False, "filter": lambda x: checkIsNumber(x) == 9}}
            present = 0
            pair = readPair(f)
            while pair not in [-1, -2]:
                key = pair["key"]
                value = pair["value"]
                if(key in fields.keys()):
                    if(not fields[key]["seen"]):
                        if(fields[key]["filter"](value)):
                            present += 1
                            fields[key] = True
                pair = readPair(f)
            if(present >= 7):
                valid += 1
            if(pair == -2):
                return valid

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
