import math

def addRungs(rungs, dist):
    required_rungs = 0
    arr = [0] + rungs
    for i in range(len(arr) - 1):
        if (arr[i+1] - arr[i]) > dist:
            n = math.ceil((arr[i+1] - arr[i])/dist) - 1
            required_rungs += n
            # using ap concept

    return required_rungs


if __name__ == '__main__':
    rungs = [3]
    dist = 1
    print(addRungs(rungs, dist))