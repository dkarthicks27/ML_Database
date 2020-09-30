'''
You are given a non-decreasing array of non-negative integers 𝑎1,𝑎2,…,𝑎𝑛. Also you are given a positive integer 𝑘.

You want to find 𝑚 non-decreasing arrays of non-negative integers 𝑏1,𝑏2,…,𝑏𝑚, such that:

The size of 𝑏𝑖 is equal to 𝑛 for all 1≤𝑖≤𝑚.
For all 1≤𝑗≤𝑛, 𝑎𝑗=𝑏1,𝑗+𝑏2,𝑗+…+𝑏𝑚,𝑗. In the other word, array 𝑎 is the sum of arrays 𝑏𝑖.
The number of different elements in the array 𝑏𝑖 is at most 𝑘 for all 1≤𝑖≤𝑚.
Find the minimum possible value of 𝑚, or report that there is no possible 𝑚.

Input
The first line contains one integer 𝑡 (1≤𝑡≤100): the number of test cases.

The first line of each test case contains two integers 𝑛, 𝑘 (1≤𝑛≤100, 1≤𝑘≤𝑛).

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (0≤𝑎1≤𝑎2≤…≤𝑎𝑛≤100, 𝑎𝑛>0).

Output
For each test case print a single integer: the minimum possible value of 𝑚. If there is no such 𝑚, print −1.
'''

