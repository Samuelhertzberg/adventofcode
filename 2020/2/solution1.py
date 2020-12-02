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
            lower = getNumber(f)
            if(lower == "EOF"):
                return totalValid
            upper = getNumber(f)
            char = f.read(1)
            number = 0
            c = f.read(2) #': '
            c = f.read(1) # first letter
            while c.isalpha():
                if(c == char):
                    number = number + 1
                c = f.read(1)
            if(lower <= number and number <= upper):
                totalValid = totalValid + 1
        
def pretty():
    with open('input') as f:
        totalValid = 0
        for line in f.readlines():
            split = re.split(' |: |-', line)
            lower = int(split[0])
            upper = int(split[1])
            char = split[2]
            count = split[3].count(char)
            if(lower <= count and count <= upper):
                totalValid = totalValid + 1
        return totalValid
        
if __name__ == '__main__':
    print(fast())
    print(pretty())