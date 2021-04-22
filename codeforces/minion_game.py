import re


def minion_game(string):
    return re.findall(r'[^aeiou].*', string)


x = minion_game('banana')
print(x)
