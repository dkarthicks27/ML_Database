n = int(input())
tot = 0

for _ in range(n):
    li = list(map(int, input().split()))
    count = sum(li)

    if count >= 2:
        tot += 1

print(tot)







