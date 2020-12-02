import re
def getNumber(f):
    number = ""
    while True:
        c = f.read(1)
        if not c:
            return "EOF"
        if c.isdigit():
            number = number + c
        else:
            return (int(number))

def fast():
    with open('input') as f:
        totalValid = 0
        while True:
            i1 = getNumber(f)
            if(i1 == "EOF"):
                return totalValid
            i2 = getNumber(f)
            char = f.read(1)
            c = f.read(2) #': '
            c = f.read(1) # first letter
            i = 1
            i1tru = False
            i2tru = False
            while c.isalpha():
                if(i == i1 and c == char):
                    i1tru = True
                if(i == i2 and c == char):
                    i2tru = True
                c = f.read(1)
                i = i + 1
            if(i1tru != i2tru):
                totalValid = totalValid + 1

def pretty():
    with open('input') as f:
        totalValid = 0
        for line in f.readlines():
            split = re.split(' |: |-', line)
            i1 = int(split[0])
            i2 = int(split[1])
            char = split[2]
            i1tru = split[3][i1-1] == char
            i2tru = split[3][i2-1] == char
            if(i1tru != i2tru):
                totalValid = totalValid + 1
        return totalValid

if __name__ == '__main__':
    print(fast())
    print(pretty())