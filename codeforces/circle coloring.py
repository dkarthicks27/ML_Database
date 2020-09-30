"""
You are given three sequences: 𝑎1,𝑎2,…,𝑎𝑛; 𝑏1,𝑏2,…,𝑏𝑛; 𝑐1,𝑐2,…,𝑐𝑛.

For each 𝑖, 𝑎𝑖≠𝑏𝑖, 𝑎𝑖≠𝑐𝑖, 𝑏𝑖≠𝑐𝑖.

Find a sequence 𝑝1,𝑝2,…,𝑝𝑛, that satisfy the following conditions:

𝑝𝑖∈{𝑎𝑖,𝑏𝑖,𝑐𝑖}
𝑝𝑖≠𝑝(𝑖mod𝑛)+1.
In other words, for each element, you need to choose one of the three possible values, such that no two adjacent elements (where we consider elements 𝑖,𝑖+1 adjacent for 𝑖<𝑛 and also elements 1 and 𝑛) will have equal value.

It can be proved that in the given constraints solution always exists. You don't need to minimize/maximize anything, you need to find any proper sequence.

Input
The first line of input contains one integer 𝑡 (1≤𝑡≤100): the number of test cases.

The first line of each test case contains one integer 𝑛 (3≤𝑛≤100): the number of elements in the given sequences.

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤100).

The third line contains 𝑛 integers 𝑏1,𝑏2,…,𝑏𝑛 (1≤𝑏𝑖≤100).

The fourth line contains 𝑛 integers 𝑐1,𝑐2,…,𝑐𝑛 (1≤𝑐𝑖≤100).

It is guaranteed that 𝑎𝑖≠𝑏𝑖, 𝑎𝑖≠𝑐𝑖, 𝑏𝑖≠𝑐𝑖 for all 𝑖.

Output
For each test case, print 𝑛 integers: 𝑝1,𝑝2,…,𝑝𝑛 (𝑝𝑖∈{𝑎𝑖,𝑏𝑖,𝑐𝑖}, 𝑝𝑖≠𝑝𝑖mod𝑛+1).

If there are several solutions, you can print any.
"""
from itertools import product
t = int(input())

output = {(1, 2, 3),
          (1, 2, 1, 2),
          (1, 3, 4, 3, 2, 4, 2),
          (1, 3, 2),
          (1, 2, 3, 1, 2, 3, 1, 2, 3, 2)}

r = 0
while r < t:
# for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    p = []

    for i in range(n):
        p.append([a[i], b[i], c[i]])

    k = product(*p)
    for i in k:
        check = False
        if i[0] == i[n - 1]:
            check = True
        else:
            for j in range(n - 1):
                if i[j] == i[j + 1]:
                    check = True
                    break

        if not check:
            if i in output:
                print(i)
                break
    r += 1

