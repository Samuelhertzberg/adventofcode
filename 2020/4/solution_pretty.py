def oneline_parse():
    return [[pair.split(":") for pair in passport] for passport in [p.split(' ') for p in (open('input_short').read().split('\n\n'))]]

def short_parse(filePWD):
    passports = (open(filePWD).read().replace('\n', ' ').split('  '))
    passports = [p.split(' ') for p in passports]
    passports = [[pair.split(":") for pair in passport] for passport in passports]
    return passports

def two_stars(filePWD):
    passports = short_parse(filePWD)
    totalValid = 0
    for passport in passports:
        fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
        presentValidFields = 0
        for pair in passport:
            if (pair[0] in fields):
                fields.remove(pair[0])
                v = pair[1]
                l = len(v)
                n = v.isnumeric()
                valid = {
                    "byr": n and l == 4 and 1920 <= int(v) <= 2002,
                    "iyr": n and l == 4 and 2010 <= int(v) <= 2020,
                    "eyr": n and l == 4 and 2010 <= int(v) <= 2030,
                    "hgt": (l == 5 and 150 <= int(v[:-2]) <= 193) if v[-2:] == "cm" else (l == 4 and 59 <= int(v[:-2]) <= 76),
                    "hcl": l ==  7 and v[:1] == "#" and len([c for c in v[1:] if c in "0123456789abcdef"]) == 6,
                    "ecl": v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                    "pid":l == 9 and n,
                    "cid": False,
                }[pair[0]]
                if(valid):
                    presentValidFields += 1
        if(presentValidFields >= 7):
            totalValid += 1
    return totalValid


        

if __name__ == '__main__':
    print(two_stars('input'))