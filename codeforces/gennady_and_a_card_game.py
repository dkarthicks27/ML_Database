def solve(tab, hand):
    for i in hand:
        if i[0] == tab[0] or i[1] == tab[1]:
            return 'YES'

    return 'NO'



if __name__ == '__main__':
    card_on_table = input()
    card_on_hand = input().split()
    ans = solve(card_on_table, card_on_hand)
    print(ans)