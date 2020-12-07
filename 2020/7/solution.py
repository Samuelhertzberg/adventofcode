import pprint
def parse(filePWD):
    with open(filePWD) as f:
        bags = {}
        for row in f.read().splitlines():
            bag = row.replace(' bags', '').replace(' bag', '').replace('.', '').split('contain ')
            bags[bag[0].strip()] = getBagOfBags(bag[1]) if bag[1] != "no other" else {}
        return bags

def getBagOfBags(string):
    return {bag[1].strip(): int(bag[0]) for bag in [bag.split(" ", 1) for bag in string.split(", ")]}
    
def countContainingBags(bags, root, key):
    if(root not in bags.keys()):
        return 0
    here = bags[root][key] if key in bags[root] else 0
    return here + sum([countContainingBags(bags, newRoot, key) for newRoot in bags[root].keys() if newRoot != key])

def countSubBags(bags, root):
    if(root not in bags.keys()):
        return 0
    return sum([countSubBags(bags, newRoot)*n + n for (newRoot, n) in bags[root].items()])

def one_star(filePWD):
    bags = parse(filePWD)
    return sum([countContainingBags(bags, bag, "shiny gold") > 0 for bag in bags.keys()])

def two_star(filePWD):
    bags = parse(filePWD)
    return countSubBags(bags, "shiny gold")


if __name__ == '__main__':
    print(one_star("input"))
    print(two_star("input"))
