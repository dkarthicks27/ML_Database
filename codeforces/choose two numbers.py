import sys

if __name__ == '__main__':

    n = int(input())
    a = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))

    global_set = set(a).union(set(b))
    for i in a:
        for j in b:
            if i + j not in global_set:
                print(i, j)
                sys.exit()



