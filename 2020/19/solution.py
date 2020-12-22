def parseRule(expr):
    if(expr[0] == "\""):
        return ("val", expr[1:-1])
    expr = expr.split(" | ")
    if(len(expr) > 1):
        return ("or", parseRule(expr[0]), parseRule(expr[1]))
    return ("set", expr[0].split(" "))

def parseFile(filePWD):
    with open(filePWD) as f:
        rules = {}
        r = f.readline()
        while(r != "\n"):
            r = r[:-1].split(": ")
            rules[r[0]] = parseRule(r[1])
            r = f.readline()
        return (rules, f.read().splitlines())

def match(expr, rule, rules):
    if(expr == "err" or expr == ""):
        return "err"
    if(rule[0] == "val"):
        if(expr[0] == rule[1]):
            return expr[1:]
        return ("err")
    if(rule[0] == "or"):
        res1 = match(expr, rule[1], rules)
        if(res1 != "err"):
            return res1
        res2 = match(expr, rule[2], rules)
        if(res2 != "err"):
            return res2
        return "err"
    if(rule[0] == "set"):
        w = expr
        for subr in rule[1]:
            w = match(w, rules[subr], rules)
        return w

def match8and11(expr, rules): #The 8 and 11 rules play together in a certain way
    instancesOf42, w = getConsRules(expr, rules['42'], rules)
    instancesOf31, w = getConsRules(w, rules['31'], rules)
    return 0 < instancesOf31 < instancesOf42 and w == ""

def getConsRules(expr, rule, rules):
    instances = 0
    w = expr
    while(True):
        t = match(w, rule, rules)
        if(t == "err"):
            return (instances, w)
        if(t == ""):
            return (instances + 1, "")
        w = t
        instances += 1

if __name__ == '__main__':
    rules, words = parseFile('input')
    print(sum([match(w, rules['0'], rules) == "" for w in words]))
    print(sum([match8and11(w, rules) for w in words]))
