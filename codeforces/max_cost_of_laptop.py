def maxCost(cost, labels, dailyCount):
    max_cost = -1
    curr_cost = 0
    num_days = 0
    for i in range(len(cost)):
        curr_cost += cost[i]
        if labels[i] == 'legal':
            num_days += 1
        # print(f'curr_cost = {curr_cost}\nnum_days = {num_days}')
        if num_days < dailyCount:
            continue

        max_cost = max(max_cost, curr_cost)
        # print(f'max_cost = {max_cost}\n')
        curr_cost = 0
        num_days = 0

    if max_cost == -1 or max_cost == 0:
        return 0

    else:
        return max_cost



n = int(input())
cost = []

for _ in range(n):
    cost.append(int(input()))

n = int(input())
labels = []

for _ in range(n):
    labels.append(input())

dc = int(input())

print(maxCost(cost, labels, dc))