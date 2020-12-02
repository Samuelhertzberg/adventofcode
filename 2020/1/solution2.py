file1 = open('data', 'r') 
Lines = file1.readlines()

parsed = {}

for line1 in Lines:
    for line2 in Lines:
        pairSum = int(line1) + int(line2)
        parsed[int(line2)] = True
        key = 2020 - pairSum
        if(key in parsed.keys()):
            print(key * int(line1) * int(line2))
            exit()