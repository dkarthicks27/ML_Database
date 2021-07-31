from math import ceil


if __name__ == '__main__':
    # lets find out the number of shelves available

    # so we know the number of medals and number of number of cups
    # first we check if there are atleast 2 shelves, one for each type
    # now we first calculate the number of medals, if
    # if medals = 15
    # no. of rows = math.ceil(18 / 10) = 2

    # so now if this is greater than n: print(no) else check if
    # remaining rows >= math.ceil(cups/5)


    cups = list(map(int, input().split()))
    medals = list(map(int, input().split()))
    k = int(input())

    num_cup_rows = ceil(sum(cups)/5)
    num_medal_rows = ceil(sum(medals)/10)
    if num_cup_rows + num_medal_rows <= k:
        print('YES')
    else:
        print('NO')
