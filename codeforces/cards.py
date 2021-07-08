from collections import Counter

if __name__ == '__main__':
    n = int(input())
    cards = input()
    x = Counter(cards)
    # so we have to make sure to make as many one's as possible

    if not x.get('n'):
        res = min(x['z'], x['e'], x['r'], x['o'])
        for i in range(res):
            print(0, sep=' ', end=' ')

    else:
        res1 = min(x['o'], x['n'], x['e'])
        res2 = min(x['z'], x['e'] - x['n'], x['r'], x['o'] - x['n'])
        for i in range(res1):
            print(1, sep=' ', end=' ')
        for i in range(res2):
            print(0, sep=' ', end=' ')