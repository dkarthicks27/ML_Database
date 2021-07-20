import math

def isvalid(s):
    # Solution of Quadratic Equation
    k = (-1 + math.sqrt(1 + 8 * s)) / 2

    # Condition to check if the
    # solution is a integer
    if math.ceil(k) == math.floor(k):
        return int(k)
    else:
        return -1


if __name__ == '__main__':
    n = int(input())
    t = input()

    i = 0
    k = 0
    ans = list(range(1, isvalid(n)+1))
    end = False
    s = ''
    while not end:
        s += t[i]
        i += ans[k]
        k += 1
        if k == isvalid(n):
            end = True

    print(s)
