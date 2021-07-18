def findSum(h):
    h.reverse()
    total = 0
    new_arr = []
    for i in h:
        new_arr.append(total+i)
        total += i

    new_arr.reverse()
    return new_arr


def shortest(n1, n2, n3):
    x = min(n1, n2, n3)
    if x == n1:
        return 0
    elif x == n2:
        return 1
    else:
        return 2

def binarySearch(item, array):
    minimum = 0
    maximum = len(array) - 1
    while minimum <= maximum:
        avg = round((maximum + minimum)/2)
        if array[avg] == item:
            return 1
        elif array[avg] < item:
            minimum = avg + 1
        elif array[avg] > item:
            maximum = avg - 1
    return 0



def equalStack(h1, h2, h3):
    s1, s2, s3 = map(findSum, [h1, h2, h3])
    sm = shortest(n1, n2, n3)
    k = [s1, s2, s3]
    s = k.pop(sm)
    sx, sy = k
    sx.sort()
    sy.sort()
    for i in s:
        if binarySearch(i, sx) and binarySearch(i, sy):
            return i

    return 0


if __name__ == '__main__':
    n1, n2, n3 = list(map(int, input().split()))
    h1 = list(map(int, input().split()))
    h2 = list(map(int, input().split()))
    h3 = list(map(int, input().split()))

    result = equalStack(h1, h2, h3)
    print(result)
