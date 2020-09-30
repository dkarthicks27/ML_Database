"""
You are given an integer 𝑛.

You should find a list of pairs (𝑥1,𝑦1), (𝑥2,𝑦2), ..., (𝑥𝑞,𝑦𝑞) (1≤𝑥𝑖,𝑦𝑖≤𝑛) satisfying the following condition.

Let's consider some function 𝑓:ℕ×ℕ→ℕ (we define ℕ as the set of positive integers). In other words, 𝑓 is a function that returns a positive integer for a pair of positive integers.

Let's make an array 𝑎1,𝑎2,…,𝑎𝑛, where 𝑎𝑖=𝑖 initially.

You will perform 𝑞 operations, in 𝑖-th of them you will:

assign 𝑡=𝑓(𝑎𝑥𝑖,𝑎𝑦𝑖) (𝑡 is a temporary variable, it is used only for the next two assignments);
assign 𝑎𝑥𝑖=𝑡;
assign 𝑎𝑦𝑖=𝑡.
In other words, you need to simultaneously change 𝑎𝑥𝑖 and 𝑎𝑦𝑖 to 𝑓(𝑎𝑥𝑖,𝑎𝑦𝑖). Note that during this process 𝑓(𝑝,𝑞) is always the same for a fixed pair of 𝑝 and 𝑞.

In the end, there should be at most two different numbers in the array 𝑎.

It should be true for any function 𝑓.

Find any possible list of pairs. The number of pairs should not exceed 5⋅105.

Input
The single line contains a single integer 𝑛 (1≤𝑛≤15000).

Output
In the first line print 𝑞 (0≤𝑞≤5⋅105) — the number of pairs.

In each of the next 𝑞 lines print two integers. In the 𝑖-th line print 𝑥𝑖, 𝑦𝑖 (1≤𝑥𝑖,𝑦𝑖≤𝑛).

The condition described in the statement should be satisfied.

If there exists multiple answers you can print any of them.
"""



def f(a, b):
    return a + b


n = 15000
array = list(range(1, n+1))
count = 0
pairs = []

for i in range(0, len(array) - 1):
    if array[i] != array[i+1]:
        t = f(array[i], array[i+1])
        pairs.append((array[i], array[i+1]))
        count += 1
        array[i] = t
        array[i+1] = t
    # print(array)


print(count)
# for i in pairs:
#     print(*i)

