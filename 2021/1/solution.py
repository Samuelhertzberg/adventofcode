def getDiffs(arr):
    return sum([arr[i] < arr[i+1] for i in range(len(arr)-1)])

def one_star(ds):
    return getDiffs(ds)

def two_star(ds):
    return getDiffs([sum(t) for t in zip(ds, ds[1:], ds[2:])])

if __name__ == '__main__':
    with open('input') as f:
        ds = [int(d) for d in f.read().split('\n')]
        print(one_star(ds))
        print(two_star(ds))
