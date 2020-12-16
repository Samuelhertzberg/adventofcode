import time
def memory(filePWD, limit):
    with open(filePWD) as f:
        nums = {int(f): i for i, f in enumerate(f.read().split(','))}
        i = len(nums)
        last = 0
        while(i < limit - 1):
            nextNumber = (i - nums[last] if last in nums else 0)
            nums[last] = i
            last = nextNumber
            i += 1
        return last

if __name__ == '__main__':
    print(memory('input', 2020))
    print(memory('input', 30000000))
