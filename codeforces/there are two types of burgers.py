if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        b, p, f = list(map(int, input().split()))
        h_cost, c_cost = list(map(int, input().split()))


        # to maximise profit
        # eqn is x * h_cost + y * c_cost:, now x + y == min(p+f, b//2)

        n = min(p+f, b//2)
        profit = 0
        for i in range(0, n+1):
            if i <= p and (n - i) <= f:
                profit = max(profit, i * h_cost + (n - i) * c_cost)

        print(profit)
