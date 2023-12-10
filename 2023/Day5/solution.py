import sys
from functools import reduce

def flatten(listOfLists):
    return [item for sublist in listOfLists for item in sublist]
 
def parseMaps(input):
    maps = input.split("\n\n")[1:]
    maps = [map.splitlines() for map in maps]
    maps = [[map.split(" ") for map in mapSet[1:]] for mapSet in maps]
    maps = [[[int(n) for n in map] for map in mapSet] for mapSet in maps]
    return [[ [src, src + l - 1, dst - src] for [dst, src, l] in mapSet] for mapSet in maps]

def parseSeedRanges(input):
    seeds = [int(n) for n in input.splitlines()[0].split(": ")[1].split(" ")]
    seeds =  list(zip(*[iter(seeds)]*2))
    return [(src, src + l - 1) for (src, l) in seeds]

def getMappedValue(mapSet, value):
    for [mapStart, mapEnd, offset] in mapSet:
        if mapStart <= value <= mapEnd:
            return value + offset
    return value

def mapRange(map, range):
    [mapStart, mapEnd, offset] = map
    (rStart, rEnd) = range
    rStartWithin = mapStart <= rStart <= mapEnd
    rEndWithin = mapStart <= rEnd <= mapEnd
    if rStartWithin and rEndWithin: # Map whole range
        return ((rStart + offset, rEnd + offset),[])
    elif rStartWithin: # Map left part of range, return right part as rest
        return ((rStart + offset, mapEnd + offset), [(mapEnd + 1, rEnd)])
    elif rEndWithin: # Map right part of range, return left part as rest
        return ((mapStart + offset, rEnd + offset), [(rStart, mapStart - 1)])
    elif rStart < mapStart and rEnd > mapEnd: # Map middle part of range, return left and right part as rest
        return ((mapStart + offset, mapEnd + offset), [(rStart, mapStart - 1), (mapEnd + 1, rEnd)])
    else: # No overlap, return range as rest
        return (None, [range])


def getMappedRange(mapSet, range):
    unMappedRanges = [range]
    mappedRanges = []
    for map in mapSet:
        nextUnMappedRanges = []
        a = [mapRange(map, unMappedRange) for unMappedRange in unMappedRanges]
        mappedRanges += [m for m, r in a if m]
        unMappedRanges = flatten([r for m, r in a])
    return mappedRanges + unMappedRanges
            

def part1(input):
    seeds = [int(n) for n in input.splitlines()[0].split(": ")[1].split(" ")]
    maps = parseMaps(input)
    for mapSet in maps:
        seeds = [getMappedValue(mapSet, seed) for seed in seeds]

    return min(seeds)

def part2(input):
    seedRanges = parseSeedRanges(input)
    maps = parseMaps(input)
    for mapSet in maps:
        seedRanges = flatten([getMappedRange(mapSet, seedRange) for seedRange in seedRanges])
    return min([r[0] for r in seedRanges])

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        input = file.read()
        print(part1(input))
        print(part2(input))