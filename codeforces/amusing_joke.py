from collections import Counter

if __name__ == '__main__':
    guest = input()
    host = input()
    pile = input()

    if Counter(guest + host) == Counter(pile):
        print('YES')
    else:
        print('NO')
