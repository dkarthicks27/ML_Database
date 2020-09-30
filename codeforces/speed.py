"""
There is a road with length 𝑙 meters. The start of the road has coordinate 0, the end of the road has coordinate 𝑙.

There are two cars, the first standing at the start of the road and the second standing at the end of the road. They will start driving simultaneously. The first car will drive from the start to the end and the second car will drive from the end to the start.

Initially, they will drive with a speed of 1 meter per second. There are 𝑛 flags at different coordinates 𝑎1,𝑎2,…,𝑎𝑛. Each time when any of two cars drives through a flag, the speed of that car increases by 1 meter per second.

Find how long will it take for cars to meet (to reach the same coordinate).

Input
The first line contains one integer 𝑡 (1≤𝑡≤104): the number of test cases.

The first line of each test case contains two integers 𝑛, 𝑙 (1≤𝑛≤105, 1≤𝑙≤109): the number of flags and the length of the road.

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 in the increasing order (1≤𝑎1<𝑎2<…<𝑎𝑛<𝑙).

It is guaranteed that the sum of 𝑛 among all test cases does not exceed 105.

Output
For each test case print a single real number: the time required for cars to meet.

Your answer will be considered correct, if its absolute or relative error does not exceed 10−6. More formally, if your answer is 𝑎 and jury's answer is 𝑏, your answer will be considered correct if |𝑎−𝑏|max(1,𝑏)≤10−6.


"""



n, l = 2, 10
pos = {1, 9}
a = []
b = []
for i in range(l+1):
    if i in pos:

