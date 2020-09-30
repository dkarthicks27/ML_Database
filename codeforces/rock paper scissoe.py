'''
Alice and Bob have decided to play the game "Rock, Paper, Scissors".

The game consists of several rounds, each round is independent of each other. In each round, both players show one of the following things at the same time: rock, paper or scissors. If both players showed the same things then the round outcome is a draw. Otherwise, the following rules applied:

if one player showed rock and the other one showed scissors, then the player who showed rock is considered the winner and the other one is considered the loser;
if one player showed scissors and the other one showed paper, then the player who showed scissors is considered the winner and the other one is considered the loser;
if one player showed paper and the other one showed rock, then the player who showed paper is considered the winner and the other one is considered the loser.
Alice and Bob decided to play exactly 𝑛 rounds of the game described above. Alice decided to show rock 𝑎1 times, show scissors 𝑎2 times and show paper 𝑎3 times. Bob decided to show rock 𝑏1 times, show scissors 𝑏2 times and show paper 𝑏3 times. Though, both Alice and Bob did not choose the sequence in which they show things. It is guaranteed that 𝑎1+𝑎2+𝑎3=𝑛 and 𝑏1+𝑏2+𝑏3=𝑛.

Your task is to find two numbers:

the minimum number of round Alice can win;
the maximum number of rounds Alice can win.
'''

import re

txt = "acabbcabjc"

# Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall(r"a.*?b.*?c", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# from itertools import permutations
# import re
#
# k = 'abcacb?abd?'
#
# p = str.replace(k, '?', 'A')
#
# n = 2
# string = 'a'*n + 'b'*n + 'c'*n
# print(string)
#
#
# def joiner(a):
#     return ''.join(a)
#
#
# l = set(list(map(joiner, list(permutations(string, n)))))
# print(l)
# print(len(l))
#
#
# for i in l:
