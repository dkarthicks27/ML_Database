if __name__ == '__main__':
    # input is a 5 X 5 matrix
    # output is the minimum number of swaps required

    for i in range(1, 6):
        li = list(map(int, input().split()))
        if 1 in li:
            indx = (i, li.index(1) + 1)
            break


    print(abs(3 - indx[0]) + abs(3 - indx[1]))