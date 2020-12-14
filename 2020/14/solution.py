import time
def getMasks(s):
    delete = int(''.join([ '1' if c == 'X' else '0' for c in s]), 2)
    insert = int(''.join([ c if c != 'X' else '0' for c in s]), 2)
    return (insert, delete)

def one_star(filePWD):
    with open(filePWD) as f:
        insert, delete = 0, 0
        mem = {}
        for l in f.read().splitlines():
            row = l.split(" = ")
            if(row[0] == "mask"):
                insert, delete = getMasks(row[1])
            else:
                adr = int(row[0].split("[")[1][:-1])     
                val = ((int(row[1]) & delete) | insert)
                mem[adr] = val
        return sum([mem[k] for k in mem.keys()])
            
def getAddresses(mask, addr):
    if(len(mask) > 0):
        rest = getAddresses(mask[1:],addr[1:])
        if(mask[0] == 'X'):
            return ['0' + comb for comb in rest] + ['1' + comb for comb in rest]
        if(mask[0] == '0'):
            return [addr[0] + comb for comb in rest]
        else:
            return ['1' + comb for comb in rest]
    else:
        return ['']

def two_star(filePWD):
    with open(filePWD) as f:
        mask = "0"*36
        mem = {}
        for l in f.read().splitlines():
            row = l.split(" = ")
            if(row[0] == "mask"):
                mask = row[1]
            else:
                init_addr = int(row[0].split("[")[1][:-1])
                for addr in getAddresses(mask, format(init_addr, "036b")):
                    mem[addr]=int(row[1])
        return sum([mem[k] for k in mem.keys()])
                

if __name__ == '__main__':
    print(one_star('input'))
    print(two_star('input'))
