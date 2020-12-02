with open('input') as f:
    totalValid = 0
    for line in f.readlines():
        a = line.split(":")
        b = a[0].split("-")
        c = b[1].split(" ")
        lower = int(b[0])
        upper = int(c[0])
        char = c[1]
        count = a[1].count(char)
        if(lower <= count and count <= upper):
            totalValid = totalValid + 1
    print(totalValid)
        