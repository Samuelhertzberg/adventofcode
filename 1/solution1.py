file1 = open('data', 'r') 
Lines = file1.readlines() 

parsed = {}

for line in Lines:
    number = int(line)
    parsed[number] = True
    complement = 2020 - number
    if(complement in parsed.keys()):
        print(complement * number)
