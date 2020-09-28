n, k = list(map(int, input().split()))

inp = list(map(int, input().split()))
key = inp[k -1]
li = [bool(s) for s in inp if s >= key]
print(sum(li))
